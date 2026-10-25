# 🌐 CodeAlpha Ruban — Language Translation Tool

A Python-based web application that translates text between different languages. This project was developed as part of the **CodeAlpha Artificial Intelligence Internship — Task 1**.

## 📌 Project Overview

CodeAlpha Ruban provides a simple interface for translating text between supported languages. Users can enter text, choose the source and target languages, and view the translated result.

The application uses Streamlit for the user interface and the MyMemory Translation API for translation.

## ✨ Features

- Translate text between supported languages.
- Choose source and target languages.
- Swap source and target languages.
- Enter and translate text through a web interface.
- Display translation results separately.
- Validate empty input.
- Handle API and connection errors.
- Clear input and translation results.
- Download translated text.
- Responsive, styled user interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web interface |
| Requests | HTTP requests to the translation API |
| MyMemory Translation API | Translation service |
| Git | Version control |
| GitHub | Source code hosting |

## 📂 Project Structure

```text
CodeAlpha_Language_Translation_Tool/
├── app.py
├── translator.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── config.toml
```

## ⚙️ Requirements

- Python 3.11 or newer
- pip
- Internet connection
- Git (for version control)

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_Language_Translation_Tool.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Open the project directory

```bash
cd CodeAlpha_Language_Translation_Tool
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment on Windows

Command Prompt:

```bash
venv\Scripts\activate.bat
```

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 📝 How to Use

1. Launch the application.
2. Select the source language.
3. Select the target language.
4. Enter the text to translate.
5. Click **Translate Text**.
6. Read the translated result.
7. Use the available controls to swap languages, clear the fields, or download the translation.

## 🧪 Testing

Test the application with different source and target languages.

Example:

- Source language: English
- Target language: Tamil
- Input: `Hello`
- Expected output: `வணக்கம்`

Also test empty input, language swapping, clearing, download functionality, and API connection failures.

Translation wording can vary, so verify results for important sentences.

## ⚠️ Limitations

- An internet connection is required.
- Translation depends on an external service.
- The free anonymous MyMemory service has usage limits.
- Translation quality may vary with the language pair and sentence context.
- The application does not train its own machine-learning model.
- The phrase dictionary, if enabled, handles only specific predefined phrases.

## 🔮 Future Enhancements

- One-click clipboard copying.
- Text-to-speech support.
- Translation history.
- Improved language detection.
- Alternative translation providers.
- More advanced translation quality evaluation.

## 🎓 Internship Information

**Organization:** CodeAlpha  
**Department:** Artificial Intelligence  
**Task:** Task 1 — Language Translation Tool

## 📄 Disclaimer

This is an educational internship project. MyMemory is an external translation service and is not affiliated with CodeAlpha.

## 👨‍💻 Author

"Ruban S."

Developed as part of the CodeAlpha Artificial Intelligence Internship.
