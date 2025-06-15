# Backend – AI on FHIR (NLP + Simulated FHIR)

This Python backend accepts natural language queries and converts them into simulated FHIR API requests.

## 🔧 Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask flask-cors spacy
python -m spacy download en_core_web_sm

