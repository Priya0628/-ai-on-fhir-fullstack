from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy

app = Flask(__name__)
CORS(app)  # Allow frontend to call this API

nlp = spacy.load("en_core_web_sm")

def parse_query(text):
    text = text.lower()
    condition = None
    age = None

    if "diabet" in text:
        condition = "diabetes"
    elif "asthma" in text:
        condition = "asthma"
    elif "cancer" in text:
        condition = "cancer"
    elif "hypertension" in text or "high blood pressure" in text:
        condition = "hypertension"

    if "over" in text or "above" in text:
        for token in nlp(text):
            if token.like_num:
                age = f">{token.text}"
                break
    elif "under" in text or "below" in text:
        for token in nlp(text):
            if token.like_num:
                age = f"<{token.text}"
                break

    return {
        "resource": "Patient",
        "conditions": [{"code": "N/A", "description": condition}],
        "filters": {"age": age}
    }

@app.route("/parse", methods=["POST"])
def parse():
    data = request.get_json()
    query = data.get("query", "")
    fhir_result = parse_query(query)
    return jsonify(fhir_result)

if __name__ == "__main__":
    app.run(debug=True)
