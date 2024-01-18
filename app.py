# run.py
from flask import Flask, render_template, request
from chatbot import chatbot

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    response = chatbot(user_input)
    return render_template("index.html", user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)
