print("🤖 Welcome to the Basic Chatbot!")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hi! Nice to meet you!")

    elif user_input == "how are you":
        print("Bot: I'm fine, thanks! How are you?")

    elif user_input == "what is your name":
        print("Bot: I'm a simple Python chatbot.")

    elif user_input == "what can you do":
        print("Bot: I can have a simple conversation with you.")

    elif user_input == "thank you" or user_input == "thanks":
        print("Bot: You're welcome!")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that.")