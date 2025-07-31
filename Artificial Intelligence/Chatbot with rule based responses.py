import tkinter as tk
from tkinter import scrolledtext
import re
from datetime import datetime
import random

# Responses dictionary for variation
responses = {
    "greeting": ["Hello there!", "Hi! How can I help you?", "Hey! Need any assistance?"],
    "identity": ["I'm a rule-based chatbot.", "I'm your assistant chatbot!", "I'm just a smart Python script 😉"],
    "help": ["Ask me about the time, weather, or just chat with me!", "I'm here to help. Try asking about the time or weather."],
    "weather": ["I'm not connected to the weather API yet, but it's sunny in here!", "Looks like clear skies... in code!"],
    "fallback": ["Hmm... I didn't get that. Could you rephrase?", "I'm not sure what you mean. Can you try again?"],
    "goodbye": ["Goodbye! Take care!", "Bye! See you soon 😊", "Farewell! Come back anytime!"]
}

# Get dynamic response
def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["bye", "exit", "quit"]:
        return random.choice(responses["goodbye"])

    elif re.search(r"\b(hi|hello|hey)\b", user_input):
        return random.choice(responses["greeting"])

    elif re.search(r"\b(who are you|your name|what can you do)\b", user_input):
        return random.choice(responses["identity"])

    elif re.search(r"\b(help|assist|support)\b", user_input):
        return random.choice(responses["help"])

    elif re.search(r"\b(time|clock)\b", user_input):
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."

    elif re.search(r"\b(weather|temperature)\b", user_input):
        return random.choice(responses["weather"])

    elif re.search(r"\b(thank you|thanks)\b", user_input):
        return "You're welcome! 😊"

    elif re.search(r"\b(how are you)\b", user_input):
        return "I'm just code, but I'm feeling helpful today!"

    elif re.search(r"\b(joke|funny)\b", user_input):
        return "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"

    else:
        return random.choice(responses["fallback"])

# Send message
def send():
    user_input = entry.get()
    if not user_input.strip():
        return

    chat_window.insert(tk.END, f"You: {user_input}\n", "user")
    response = get_bot_response(user_input)
    chat_window.insert(tk.END, f"Bot: {response}\n\n", "bot")
    entry.delete(0, tk.END)
    chat_window.see(tk.END)

# GUI setup
root = tk.Tk()
root.title("Smart Chatbot 🤖")
root.geometry("500x600")
root.resizable(False, False)

# Chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25, font=("Segoe UI", 11))
chat_window.pack(pady=10)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")
chat_window.insert(tk.END, "Bot: Hello! I'm your assistant. How can I help you?\n\n", "bot")

# Entry field
entry = tk.Entry(root, width=50, font=("Segoe UI", 12))
entry.pack(pady=5)
entry.bind("<Return>", lambda event: send())

# Send button
send_button = tk.Button(root, text="Send", command=send, width=10, font=("Segoe UI", 12))
send_button.pack(pady=5)

root.mainloop()
