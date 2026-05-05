# VoiceScribe 🎙️
**An AI-Powered Speech-to-Text, Translation, and Productivity Tool for Indian Languages**

VoiceScribe is a comprehensive web application designed to bridge the language gap and improve productivity. It allows users to convert spoken words or uploaded documents into text, seamlessly translate them into multiple Indian languages, and apply AI-driven productivity tools like summarization and formatting.

## 🚀 Key Features

### 1. Real-Time Speech-to-Text
- Instantly converts spoken voice into text using Google's Speech Recognition engine.
- Supports recording audio directly from the browser or uploading pre-recorded audio files (`.wav`, `.mp3`, `.m4a`).

### 2. Multi-Language Translation
- Translates transcribed or extracted text into major Indian languages including **Hindi, Kannada, Tamil, Telugu, Malayalam, Marathi, Bengali, and Gujarati**.
- Built-in Text-to-Speech (TTS) allows users to listen to the translated output.

### 3. Document Parsing (OCR & Text Extraction)
- Users can upload **PDFs, Word Documents (.docx), and plain text files (.txt)**.
- The system automatically extracts the text from these documents, allowing users to translate or summarize long files without manual typing.

### 4. AI Productivity Tools
- **📝 AI Summarization**: Uses Natural Language Processing (NLP) via the `sumy` library (LSA Summarizer) to generate concise, bulleted summaries of long lectures or documents.
- **✨ Smart Formatting**: Automatically formats raw, lowercase speech-to-text output by adding proper capital letters and punctuation.

### 5. Advanced Export Options
- **Subtitle Generator (.SRT)**: Automatically calculates timestamps and exports the transcription as a professional subtitle file for video editing.
- **PDF Export**: Generates perfectly formatted PDFs with native Unicode font support (Noto Sans) so Indian scripts render flawlessly without encoding errors (`????`).
- **Word (.docx) & TXT Export**: Allows downloading the text for offline use.

---

## 🛠️ Technology Stack
- **Frontend**: HTML5, Vanilla JavaScript, CSS3 (Custom Glassmorphism UI)
- **Backend**: Python, Flask
- **Machine Learning & NLP**:
  - `SpeechRecognition`: Audio transcription
  - `deep-translator`: Multi-lingual translation
  - `sumy` & `nltk`: Extractive text summarization
- **File Processing**:
  - `PyPDF2`: PDF text extraction
  - `python-docx`: Word document reading and writing
  - `fpdf2`: Custom PDF generation with Unicode fonts
- **Deployment**: Gunicorn (WSGI HTTP Server) configured for cloud hosting (Render.com)

---

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/akshaynelgundh2007-png/VoiceScribe.git
   cd VoiceScribe
   ```

2. **Install Dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python app.py
   ```
   *The server will start on `http://127.0.0.1:5000/`*

---

## 🎓 Academic Value & Use Case
This project was designed as a highly productive case study. It solves two major real-world problems:
1. **Accessibility**: It breaks down language barriers by allowing real-time translation of spoken words into regional Indian languages.
2. **Productivity**: It acts as an automated "Meeting Minutes" generator. By utilizing NLP summarization and automated subtitle (.srt) generation, it transforms raw audio/documents into actionable, structured data.