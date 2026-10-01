# EduGenie - Google Gemini Powered Learning Assistant

EduGenie is a lightweight educational assistant based on the supplied project document.

## Features

- Q&A using Google Gemini
- Concept explanation using the documented LaMini-Flan-T5 local model, with Gemini fallback
- Three-question MCQ quiz generation
- Educational text summarization
- Beginner-to-advanced learning paths
- FastAPI REST endpoints
- HTML + CSS frontend
- Simple browser-based interaction

## Folder structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Prerequisites

The supplied documentation specifies Python 3.10+, FastAPI, HTML/CSS, a Google Gemini API key, Uvicorn, and Jinja2.

## VS Code setup

### 1. Open the project

Open the `EduGenie` folder in VS Code.

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The first explanation request may download the local LaMini-Flan-T5 model from Hugging Face, so the first run can take longer.

### 4. Configure the API key

Copy `.env.example` to `.env` and set:

```text
GEMINI_API_KEY=YOUR_KEY_HERE
GEMINI_MODEL=gemini-1.5-pro
```

If the model name specified by the supplied document is no longer available in your Google AI account, set `GEMINI_MODEL` to a currently available Gemini model.

Never commit `.env` or expose the API key in frontend code.

### 5. Start the server

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## API endpoints

- `POST /qa`
- `POST /explain`
- `POST /quiz`
- `POST /summarize`
- `POST /learn/recommendations`
- `GET /health`

Each POST endpoint accepts JSON such as:

```json
{
  "text": "Explain the Pythagoras theorem"
}
```

## Functional testing

1. Q&A: ask a general academic question.
2. Explain: enter a topic such as "photosynthesis".
3. Quiz: enter a passage and verify that 3 questions with 4 options are returned.
4. Summary: paste a long educational paragraph.
5. Recommend Path: enter a topic such as "SQL" and check the beginner-to-advanced plan.

## Notes

The supplied document describes Gemini 1.5 Pro and LaMini-Flan-T5-783M. The implementation keeps those choices configurable through `.env` so the project can be adjusted if an account no longer exposes the exact documented Gemini model name.
