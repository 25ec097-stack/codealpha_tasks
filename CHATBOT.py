def get_response(message):
    message = message.lower()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return "Hi there! Nice to meet you."

    elif "how are you" in message:
        return "I'm doing great! Thanks for asking. How about you?"

    elif "fine" in message or "good" in message:
        return "Glad to hear that!"

    elif "sad" in message or "not good" in message:
        return "Oh no! I'm here if you want to talk."

    elif "your name" in message:
        return "I'm ChatBuddy, your simple chatbot friend!"

    elif "help" in message:
        return "I can greet you, chat with you, and say goodbye. Try saying 'hello' or 'bye'."

    elif any(word in message for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Take care "

    else:
        return "Hmm, I didn't understand that. Try asking something else."

def chatbot():
    print("========== BASIC CHATBOT ==========")
    print("Chat with me! Type 'bye' anytime to exit.\n")

    while True:
        user_msg = input("You: ")
        response = get_response(user_msg)
        print("Bot:", response)

        if "bye" in user_msg.lower() or "goodbye" in user_msg.lower():
            break

    print("\n========== CHAT ENDED ==========")

chatbot()
