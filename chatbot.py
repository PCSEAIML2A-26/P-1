# chatbot.py
import spacy
import json
from fuzzywuzzy import fuzz
from random import choice

nlp = spacy.load("en_core_web_sm")

with open("intents.json", "r") as file:
    intents_data = json.load(file)
    intents = intents_data.get("intents", [])

def find_intent(user_input):
    best_match = {"tag": None, "score": 0}

    for intent in intents:
        for pattern in intent.get("patterns", []):
            similarity_score = fuzz.token_set_ratio(user_input, pattern)
            if similarity_score > best_match["score"]:
                best_match["tag"] = intent["tag"]
                best_match["score"] = similarity_score

    return best_match["tag"] if best_match["score"] > 60 else None

def get_response(intent_tag):
    for intent in intents:
        if intent["tag"] == intent_tag:
            responses = intent.get("responses", [])
            return choice(responses) if responses else None

    return None

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