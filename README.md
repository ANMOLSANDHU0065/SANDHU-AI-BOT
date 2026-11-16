# SANDHU AI BOT

A beginner-friendly NLP chatbot web application built with Python, Flask, scikit-learn (TF-IDF), and SQLite.

## Features

- Chat interface built with HTML, CSS, and JavaScript
- NLP-based FAQ matching using TF-IDF and cosine similarity
- Basic follow-up context handling
- SQLite chat history, separated by browser session
- Clear chat feature
- Responsive layout
- Simple tests with pytest

## Important project note

This starter project uses a lightweight retrieval-based NLP engine. It is an AI/NLP learning chatbot, but it is **not** a generative LLM like ChatGPT. The Hugging Face / Transformers integration can be added as a later enhancement with a suitable model and API configuration.

## Requirements

- Python 3.10 or newer
- VS Code (recommended)

## Setup on Windows PowerShell

Open this folder in VS Code and run:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python run.py
```

If PowerShell blocks activation, run this in the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

Then open http://127.0.0.1:5000 in your browser.

## Run tests

```powershell
pytest
```

## Project structure

```text
SANDHU-AI-BOT/
├── backend/
│   ├── routes/
│   ├── app.py
│   ├── chatbot.py
│   ├── config.py
│   ├── database.py
│   └── nlp_engine.py
├── frontend/
│   ├── templates/
│   └── static/
├── database/          # chatbot.db is created automatically
├── models/            # place optional model assets here
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── run.py
```

## Customizing answers

Edit the `FAQS` list in `backend/nlp_engine.py` to add your own sample questions and answers. Keep each question group short and add several natural ways a user might ask the same thing.

## Before publishing

- Change the `SECRET_KEY` in `.env` to a secure random value.
- Do not upload `.env` or database files to GitHub.
- Add your own screenshots to the README.
- Test the app and explain honestly that the current version uses TF-IDF FAQ retrieval.
