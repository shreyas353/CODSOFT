import tkinter as tk
from tkinter import messagebox

# Main application window
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x500")
root.config(bg="#f5f5f5")

tasks = []

# Functions
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        task = tasks[selected[0]]
        if not task.startswith("✔️ "):
            tasks[selected[0]] = "✔️ " + task
            update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# GUI Layout
tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f5f5f5").pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), width=24)
entry.pack(pady=10)

btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Task", width=10, command=add_task, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_task, bg="#f44336", fg="white").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Mark Done", width=10, command=mark_done, bg="#2196F3", fg="white").grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, font=("Helvetica", 14), height=15, width=40, selectbackground="#D3D3D3")
listbox.pack(pady=10)

root.mainloop()