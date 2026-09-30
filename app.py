from flask import Flask, request, jsonify, send_file
from ollama import chat

app = Flask(__name__)


@app.route("/")
def home():
    return send_file("index.html")


@app.route("/style.css")
def css():
    return send_file("style.css")


@app.route("/script.js")
def javascript():
    return send_file("script.js")


@app.route("/chat", methods=["POST"])
def chatbot():

    data = request.get_json()
    user_message = data["message"]

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return jsonify({
        "response": response["message"]["content"]
    })


if __name__ == "__main__":
    app.run(debug=True)