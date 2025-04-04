def chatbot():
    print("Chatbot: Hello! I'm your friendly assistant. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hey there! How can I assist you?")

        elif "your name" in user_input:
            print("Chatbot: I'm ChatBuddy, your simple chatbot friend.")

        elif "how are you" in user_input:
            print("Chatbot: I'm doing great! Thanks for asking.")

        elif "help" in user_input:
            print("Chatbot: I can answer questions like time, date, weather (basic), or daily queries.")

        elif "weather" in user_input:
            print("Chatbot: I'm not connected to live weather updates, but I hope it's nice outside!")

        elif "time" in user_input:
            from datetime import datetime
            print("Chatbot: The current time is", datetime.now().strftime("%I:%M %p"))

        elif "date" in user_input or "day" in user_input:
            from datetime import datetime
            print("Chatbot: Today is", datetime.now().strftime("%A, %B %d, %Y"))

        elif "what should i eat" in user_input:
            print("Chatbot: Something light and healthy is always a good choice!")

        elif "how was your day" in user_input:
            print("Chatbot: It's been productive! Thanks for asking.")

        elif "what are you doing" in user_input:
            print("Chatbot: Just waiting to help you out!")

        elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
            print("Chatbot: Goodbye! Take care.")
            break

        else:
            print("Chatbot: Hmm... I didn’t quite understand that. Try something else!")
chatbot()
