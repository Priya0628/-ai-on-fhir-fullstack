# 🧠 AI on FHIR – Natural Language Healthcare Query Tool

This is a full-stack project that simulates querying a FHIR-compliant healthcare system using **natural language**.

Type a query like:

> _“Show me all diabetic patients over 50”_

…and the system will extract the intent and simulate a FHIR API call to return relevant patient data. You’ll see results in both a **chart** and a 
**table**.

---

## 🌟 Features

- 🔎 Natural language query input
- 🧠 NLP-based intent/entity extraction (spaCy)
- 🧪 Simulated FHIR API response (Patient + Condition)
- 📊 Frontend with chart and table
- ☁️ Deployed via Vercel
- 🔐 HIPAA compliance write-up

---

## 🛠️ Technologies Used

**Backend**
- Python + Flask
- spaCy (for NLP)
- CORS for frontend communication

**Frontend**
- Next.js (React framework)
- TypeScript
- Chart.js for visualization

**Deployment**
- GitHub (source code)
- Vercel (frontend hosting)

---

## 🧩 Folder Structure


---

## 💡 How I Built It

### Backend
1. Set up a Flask server.
2. Used spaCy to extract medical condition (like “diabetes”) and age filter from queries.
3. Simulated a FHIR API response based on mock data.
4. Created a `/query` endpoint to accept natural language and return patient info.

### Frontend
1. Built a UI in Next.js inside `frontend/fhir-ui`.
2. Created an input box and submit button for the user query.
3. Displayed results in a **table** and **bar chart**.
4. Connected to the Flask API using `fetch`.

### Deployment
1. Pushed all code to GitHub.
2. Set up Vercel deployment with `frontend/fhir-ui` as the root directory.
3. Live link is below!

---

## 🌐 Live Demo

👉 [Try it here on Vercel](https://ai-on-fhir-fullstack-d5dp.vercel.app)

---

## 🔐 HIPAA & Security

See `docs/hipaa_compliance.md` for a brief technical write-up covering:
- OAuth 2.0 / SMART on FHIR
- RBAC (Role-based access control)
- Data privacy & audit logging

---

## ✅ How to Run Locally

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # or manually: flask, flask-cors, spacy
python3 app.py

