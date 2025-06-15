import spacy

# Load the small English NLP model
nlp = spacy.load("en_core_web_sm")

# A very simple function to simulate mapping a query to a FHIR API structure
def parse_query(text):
    text = text.lower()
    doc = nlp(text)

    # Initialize condition and age filters
    condition = None
    age_filter = None

    # Simple keyword matching for conditions
    if "diabet" in text:
        condition = "diabetes"
    elif "asthma" in text:
        condition = "asthma"
    elif "cancer" in text:
        condition = "cancer"
    elif "hypertension" in text or "high blood pressure" in text:
        condition = "hypertension"

    # Handle age phrases
    if "over" in text or "above" in text:
        for token in doc:
            if token.like_num:
                age_filter = f">{token.text}"
                break
    elif "under" in text or "below" in text:
        for token in doc:
            if token.like_num:
                age_filter = f"<{token.text}"
                break

    # Simulated FHIR query structure
    simulated_fhir_query = {
        "resource": "Patient",
        "conditions": [
            {
                "code": "N/A",  # In real app: ICD-10 or SNOMED code
                "description": condition
            }
        ],
        "filters": {
            "age": age_filter
        }
    }

    return simulated_fhir_query

# Test with multiple example queries
if __name__ == "__main__":
    example_queries = [
        "Show me all diabetic patients over 50",
        "List patients with asthma under 30",
        "Find cancer patients above 60 years old",
        "Patients with hypertension below 45"
    ]

    for query in example_queries:
        print("Input Query:", query)
        print("Simulated FHIR Request:", parse_query(query))
        print("----")
