import streamlit as st
from translator import translate_text

st.set_page_config(
    page_title="CodeAlpha Ruban | Language Translator",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)




st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(
                135deg,
                #f5f8ff 0%,
                #eef4ff 100%
            );
        }

        .main-title {
            text-align: center;
            font-size: 42px;
            font-weight: 800;
            color: #173b70;
            margin-bottom: 5px;
        }

        .subtitle {
            text-align: center;
            color: #526783;
            font-size: 17px;
            margin-bottom: 30px;
        }

        .section-title {
            color: #173b70;
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .info-box {
            background: #ffffff;
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #d9e4f5;
            margin-bottom: 15px;
        }

        .footer {
            text-align: center;
            color: #65758b;
            font-size: 13px;
            padding-top: 30px;
        }

        div.stButton > button {
            border-radius: 10px;
            font-weight: 600;
            min-height: 42px;
        }
    </style>
    """,
    unsafe_allow_html=True
)




LANGUAGES = {
    
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Bengali": "bn",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Swahili": "sw"
}




if "source_language" not in st.session_state:
    st.session_state.source_language = "English"

if "target_language" not in st.session_state:
    st.session_state.target_language = "Tamil"

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""




st.markdown(
    '<div class="main-title">🌐 CodeAlpha Ruban </div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Break language barriers with simple and fast translation.
        <br>
        Enter your text, choose your languages, and translate.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()




language_names = list(LANGUAGES.keys())

source_col, swap_col, target_col = st.columns(
    [5, 1, 5],
    vertical_alignment="bottom"
)

with source_col:
    st.markdown(
        '<div class="section-title">From</div>',
        unsafe_allow_html=True
    )

    st.selectbox(
        "Source language",
        options=language_names,
        key="source_language",
        label_visibility="collapsed"
    )

with swap_col:
    st.markdown("<br>", unsafe_allow_html=True)

    swap_clicked = st.button(
        "⇄",
        help="Swap source and target languages",
        use_container_width=True
    )

    if swap_clicked:
        if True:
            old_source = st.session_state.source_language

            st.session_state.source_language = (
                st.session_state.target_language
            )

            st.session_state.target_language = old_source

            st.session_state.translated_text = ""

            st.rerun()
        else:
            st.warning(
                "Choose a specific source language before swapping."
            )

with target_col:
    st.markdown(
        '<div class="section-title">To</div>',
        unsafe_allow_html=True
    )

    st.selectbox(
        "Target language",
        options=language_names,
        key="target_language",
        label_visibility="collapsed"
    )



left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown("### ✍️ Enter your text")

    st.text_area(
        "Text to translate",
        placeholder="Type or paste your text here...",
        height=250,
        key="input_text",
        max_chars=5000,
        label_visibility="collapsed"
    )

    current_length = len(st.session_state.input_text)

    st.caption(f"{current_length} / 5000 characters")

with right_col:
    st.markdown("### 📝 Translation result")

    if st.session_state.translated_text:
        st.text_area(
            "Translated text",
            value=st.session_state.translated_text,
            height=250,
            key="output_display",
            disabled=True,
            label_visibility="collapsed"
        )
    else:
        st.info(
            "Your translated text will appear here after translation."
        )



translate_col, copy_col, clear_col = st.columns(
    [2, 1, 1]
)

with translate_col:
    translate_clicked = st.button(
        "🌍 Translate Text",
        type="primary",
        use_container_width=True
    )

with copy_col:
    copy_clicked = st.button(
        "📋 Copy Result",
        use_container_width=True,
        disabled=not bool(st.session_state.translated_text)
    )

with clear_col:
    clear_clicked = st.button(
        "🗑️ Clear",
        use_container_width=True
    )


# --------------------------------------------------
# TRANSLATION PROCESS
# --------------------------------------------------

if translate_clicked:
    original_text = st.session_state.input_text.strip()

    if not original_text:
        st.warning("Please enter some text before translating.")

    elif (
        st.session_state.source_language
        == st.session_state.target_language
        and st.session_state.source_language != "Auto Detect"
    ):
        st.warning(
            "Source and target languages are the same. "
            "Please select different languages."
        )

    else:
        source_code = LANGUAGES[
            st.session_state.source_language
        ]

        target_code = LANGUAGES[
            st.session_state.target_language
        ]

        try:
            with st.spinner("Translating your text..."):
                result = translate_text(
                    original_text,
                    source_code,
                    target_code
                )

            st.session_state.translated_text = result

            st.success("Translation completed successfully!")

            st.rerun()

        except Exception as error:
            st.error(str(error))


# --------------------------------------------------
# COPY AND CLEAR
# --------------------------------------------------

if copy_clicked:
    st.code(
        st.session_state.translated_text,
        language=None
    )

    st.caption(
        "Select the translated text above and copy it. "
        "For a direct clipboard button, use the browser's "
        "copy controls or add a clipboard component."
    )

if clear_clicked:
    st.session_state.input_text = ""
    st.session_state.translated_text = ""

    st.rerun()


# --------------------------------------------------
# PROJECT INFORMATION
# --------------------------------------------------

st.divider()

with st.expander("ℹ️ About this project"):
    st.write(
        """
        CodeAlpha Ruban is a Python-based language translation
        application developed as part of the CodeAlpha
        Artificial Intelligence Internship.

        Features:
        - Multiple language options
        - Automatic source language detection
        - Translation using an external translation service
        - Language swapping
        - Text input validation
        - Error handling
        - Simple and responsive user interface
        """
    )

st.markdown(
    """
    <div class="footer">
        CodeAlpha AI Internship | Task 1: Language Translation Tool
        <br>
        Developed using Python and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
