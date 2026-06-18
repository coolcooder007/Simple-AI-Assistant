import random

responses = {
    "hello": [
        "Hi there! 👋",
        "Hello! How can I help you?",
        "Hey! Nice to meet you."
    ],
    "how are you": [
        "I'm doing great! 😊",
        "All systems operational! 🤖",
        "I'm fine, thanks for asking!"
    ],
    "bye": [
        "Goodbye! 👋",
        "See you later!",
        "Have a great day!"
    ]
}

print("🤖 Simple AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if "bye" in user:
        print("Bot:", random.choice(responses["bye"]))
        break

    found = False

    for key in responses:
        if key in user:
            print("Bot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        generic = [
            "That's interesting!",
            "Tell me more about that.",
            "I see. What else would you like to discuss?",
            "Can you explain that differently?"
        ]
        import random

print("Bot:", random.choice(generic))

responses = {
    "hello": [
        "Hi there! 👋",
        "Hello! How can I help you?",
        "Hey! Nice to meet you."
    ],
    "how are you": [
        "I'm doing great! 😊",
        "All systems operational! 🤖",
        "I'm fine, thanks for asking!"
    ],
    "bye": [
        "Goodbye! 👋",
        "See you later!",
        "Have a great day!"
    ]
}

print("🤖 Simple AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if "bye" in user:
        print("Bot:", random.choice(responses["bye"]))
        break

    found = False

    for key in responses:
        if key in user:
            print("Bot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        generic = [
            "That's interesting!",
            "Tell me more about that.",
            "I see. What else would you like to discuss?",
            "Can you explain that differently?"
        ]
        print("Bot:", random.choice(generic))
