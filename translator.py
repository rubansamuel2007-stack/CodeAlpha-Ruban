
import requests
import html
import re


API_URL = "https://api.mymemory.translated.net/get"

# Verified phrase translations for common English-to-Tamil inputs.
# Keys are normalized to lowercase without surrounding punctuation.
COMMON_TRANSLATIONS = {
    ("en", "ta", "hello"): "வணக்கம்",
    ("en", "ta", "hi"): "வணக்கம்",
    ("en", "ta", "how are you"): "நீங்கள் எப்படி இருக்கிறீர்கள்?",
    ("en", "ta", "how are you?"): "நீங்கள் எப்படி இருக்கிறீர்கள்?",
    ("en", "ta", "i am fine"): "நான் நலமாக இருக்கிறேன்.",
    ("en", "ta", "i am fine."): "நான் நலமாக இருக்கிறேன்.",
    ("en", "ta", "thank you"): "நன்றி",
    ("en", "ta", "good morning"): "காலை வணக்கம்",
    ("en", "ta", "good night"): "இனிய இரவு",
    ("en", "ta", "what is your name"): "உங்கள் பெயர் என்ன?",
    ("en", "ta", "my name is ruban"): "என் பெயர் ரூபன்.",
    ("en", "ta", "i love you"): "நான் உன்னை நேசிக்கிறேன்.",
    ("en", "ta", "where are you"): "நீங்கள் எங்கே இருக்கிறீர்கள்?",
    ("en", "ta", "welcome"): "நல்வரவு",
    ("en", "ta", "sorry"): "மன்னிக்கவும்",
    ("en", "ta", "please help me"): "தயவுசெய்து எனக்கு உதவுங்கள்.",
    ("en", "ta", "what are you doing"): "நீங்கள் என்ன செய்கிறீர்கள்?",
    ("en", "ta", "see you tomorrow"): "நாளை சந்திப்போம்.",
    ("en", "ta", "i am happy"): "நான் மகிழ்ச்சியாக இருக்கிறேன்.",
    ("en", "ta", "good afternoon"): "மதிய வணக்கம்",
    ("ta", "en", "வணக்கம்"): "Hello",
    ("ta", "en", "நன்றி"): "Thank you",
    ("ta", "en", "நீங்கள் எப்படி இருக்கிறீர்கள்"): "How are you?",
    ("ta", "en", "நான் நலமாக இருக்கிறேன்"): "I am fine.",
}


def normalize_text(text):
    """Normalize whitespace and punctuation for phrase lookup."""
    text = re.sub(r"\s+", " ", text.strip())
    return text.rstrip("?.!,;:").casefold()


def split_text(text, max_bytes=400):
    """Split long text into UTF-8-safe chunks at word boundaries."""
    chunks = []
    current = ""

    for word in text.split():
        candidate = f"{current} {word}".strip()

        if len(candidate.encode("utf-8")) <= max_bytes:
            current = candidate
        else:
            if current:
                chunks.append(current)

            if len(word.encode("utf-8")) > max_bytes:
                raise ValueError(
                    "A single word is too long to translate safely."
                )

            current = word

    if current:
        chunks.append(current)

    return chunks


def translate_with_mymemory(text, source_language, target_language):
    """Translate text using the MyMemory API."""

    translated_chunks = []

    for chunk in split_text(text):
        response = requests.get(
            API_URL,
            params={
                "q": chunk,
                "langpair": (
                    f"{source_language}|{target_language}"
                ),
            },
            timeout=20,
        )

        response.raise_for_status()
        data = response.json()

        if data.get("responseStatus") != 200:
            raise RuntimeError(
                data.get(
                    "responseDetails",
                    "The translation service rejected the request."
                )
            )

        result = data.get("responseData", {}).get("translatedText")

        if not result:
            raise RuntimeError(
                "The translation service returned an empty result."
            )

        translated_chunks.append(html.unescape(result))

    return " ".join(translated_chunks)


def translate_text(text, source_language, target_language):
    """
    Translate text using exact phrase matches first,
    then use MyMemory for other sentences.
    """

    if not text or not text.strip():
        raise ValueError("Please enter some text to translate.")

    if source_language == "auto":
        raise ValueError(
            "Please select the source language explicitly."
        )

    if source_language == target_language:
        raise ValueError(
            "Please select two different languages."
        )

    original_text = text.strip()
    normalized = normalize_text(original_text)

    # Exact phrase lookup avoids unreliable API results for these phrases.
    key = (source_language, target_language, normalized)

    if key in COMMON_TRANSLATIONS:
        return COMMON_TRANSLATIONS[key]

    # Use the API for other text.
    try:
        result = translate_with_mymemory(
            original_text,
            source_language,
            target_language
        )

        # Do not silently return an obvious unchanged error response.
        if not result or not result.strip():
            raise RuntimeError("The translation result is empty.")

        return result

    except requests.Timeout as error:
        raise RuntimeError(
            "The translation request timed out. Please try again."
        ) from error

    except requests.RequestException as error:
        raise RuntimeError(
            "Unable to connect to the translation service. "
            "Check your internet connection and try again."
        ) from error

    except (ValueError, RuntimeError):
        raise

    except Exception as error:
        raise RuntimeError(
            "Translation failed. Please try again later."
        ) from error
