from flask import Flask, render_template, request, jsonify
import spacy
import json
from fuzzywuzzy import fuzz
from random import choice

app = Flask(__name__)

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Load the intents from the JSON file
with open("intents.json", "r") as file:
    intents_data = json.load(file)
    intents = intents_data.get("intents", [])

# Function to find the best matching intent based on user input
def find_intent(user_input):
    best_match = {"tag": None, "score": 0}

    for intent in intents:
        for pattern in intent.get("patterns", []):
            similarity_score = fuzz.token_set_ratio(user_input, pattern)
            if similarity_score > best_match["score"]:
                best_match["tag"] = intent["tag"]
                best_match["score"] = similarity_score

    return best_match["tag"] if best_match["score"] > 60 else None

# Function to get a response for a given intent tag
def get_response(intent_tag):
    for intent in intents:
        if intent["tag"] == intent_tag:
            responses = intent.get("responses", [])
            return choice(responses) if responses else None

    return None

# Main chatbot function
def chatbot(user_input):
    user_input = user_input.lower()
    intent_tag = find_intent(user_input)

    if intent_tag:
        response = get_response(intent_tag)
        return response

    return choice([
        "Sorry, I didn't understand you.",
        "Please go on.",
        "Not sure I understand that.",
        "Please don't hesitate to talk to me."
    ])

# Flask routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    user_input = request.form.get("user_input")
    response = chatbot(user_input)
    return jsonify({"user_input": user_input, "response": response})

if __name__ == "__main__":
    app.run(debug=True)
