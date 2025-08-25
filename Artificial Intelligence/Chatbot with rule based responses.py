import tkinter as tk
from tkinter import scrolledtext
import re
from datetime import datetime
import random

# Responses dictionary
responses = {
    "greeting": ["Hello there!", "Hi! How can I help you?", "Hey! Need any assistance?"],
    "identity": ["I'm a rule-based chatbot.", "I'm your QnA assistant chatbot!", "I'm just a smart Python script 😉"],
    "help": ["Ask me about the time, weather, or just chat with me!", "I'm here to help. Try asking about the time or weather."],
    "weather": ["I'm not connected to live weather API yet, but it's sunny in here!", "Clear skies... in my code world 🌤️"],
    "jokes": [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why was the math book sad? Because it had too many problems.",
        "Why did the computer go to the doctor? Because it caught a virus!"
    ],
    "mood": ["I'm feeling fantastic today!", "Running smoothly, thanks for asking!", "Happy to assist you 😃"],
    "compliment": ["You're awesome!", "You're doing great!", "Keep it up, champ! 💪"],
    "goodbye": ["Goodbye! Take care!", "Bye! See you soon 😊", "Farewell! Come back anytime!"],
    "fallback": ["Hmm... I didn't get that. Could you rephrase?", "I'm not sure what you mean. Can you try again?"]
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

    elif re.search(r"\b(how are you|mood)\b", user_input):
        return random.choice(responses["mood"])

    elif re.search(r"\b(joke|funny)\b", user_input):
        return random.choice(responses["jokes"])

    elif re.search(r"\b(compliment|praise)\b", user_input):
        return random.choice(responses["compliment"])

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

# Clear chat
def clear_chat():
    chat_window.delete(1.0, tk.END)
    chat_window.insert(tk.END, "Bot: 👋 Hello! I'm your QnA Assistant.\nAsk me questions like 'time', 'joke', 'weather', or just chat!\n\n", "bot")

# Exit app
def exit_chat():
    root.destroy()

# Fullscreen toggle
def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", True)

def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)

# GUI setup
root = tk.Tk()
root.title("QnA Chatbot 🤖")
root.geometry("1000x700")

# Bind keys for fullscreen
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", exit_fullscreen)

# Chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 12), bg="#f0f0f0")
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")
chat_window.insert(tk.END, "Bot: 👋 Hello! I'm your QnA Assistant.\nAsk me questions like 'time', 'joke', 'weather', or just chat!\n\n", "bot")

# Entry + buttons frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X, pady=10)

entry = tk.Entry(bottom_frame, font=("Segoe UI", 12))
entry.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.X, expand=True)
entry.bind("<Return>", lambda event: send())

send_button = tk.Button(bottom_frame, text="Send", command=send, font=("Segoe UI", 12), bg="#4CAF50", fg="white", width=10)
send_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(bottom_frame, text="Clear Chat", command=clear_chat, font=("Segoe UI", 12), bg="#2196F3", fg="white", width=12)
clear_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(bottom_frame, text="Exit", command=exit_chat, font=("Segoe UI", 12), bg="#f44336", fg="white", width=10)
exit_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
