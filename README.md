# Deployment Test

Full Streamlit chatbot project with separate `backend` and `frontend` folders.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a local `.env` file:

```text
OPENAI_API_KEY=your_openai_api_key_here
```

## Run Backend

```powershell
python -m backend.main
```

## Run Frontend

```powershell
streamlit run frontend/app.py
```
