from ollama import chat

print("🤖 AI Chatbot")
print("Type 'bye' to exit.")

while True:
    user_message = input("You: ")

    if user_message.lower() == "bye":
        print("Bot: Goodbye! 👋")
        break

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    print("Bot:", response["message"]["content"])