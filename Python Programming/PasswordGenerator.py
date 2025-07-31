import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be positive.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password:\n{password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter password length:", font=("Arial", 12)).pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="green", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
result_label.pack()

root.mainloop()