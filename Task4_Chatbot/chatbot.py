# Basic Rule-Based Chatbot

print("================================")
print("       BASIC CHATBOT")
print("================================")
print("Hello! I am a simple chatbot.")
print("You can say hello, ask how I am, say thanks, or say goodbye.")
print("Type 'bye' to exit.\n")

while True:

    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hi! Nice to meet you.")

    elif "how are you" in user_input:
        print("Bot: I am fine, thank you!")

    elif "thanks" in user_input or "thank you" in user_input:
        print("Bot: You're welcome!")

    elif user_input == "bye" or user_input == "goodbye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")

    print()