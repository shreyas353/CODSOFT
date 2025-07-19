import tkinter as tk
from tkinter import ttk, messagebox

# Arithmetic operation functions
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Math Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Invalid Operation", "Please select a valid operation.")
            return

        label_result.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create main window
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("350x300")
root.configure(bg="#f0f0f0")

# Labels and Entry fields
tk.Label(root, text="Enter first number:", bg="#f0f0f0", font=('Arial', 12)).pack(pady=5)
entry_num1 = tk.Entry(root, font=('Arial', 12))
entry_num1.pack(pady=5)

tk.Label(root, text="Enter second number:", bg="#f0f0f0", font=('Arial', 12)).pack(pady=5)
entry_num2 = tk.Entry(root, font=('Arial', 12))
entry_num2.pack(pady=5)

tk.Label(root, text="Select operation:", bg="#f0f0f0", font=('Arial', 12)).pack(pady=5)
operation_var = tk.StringVar()
operation_menu = ttk.Combobox(root, textvariable=operation_var, font=('Arial', 12))
operation_menu['values'] = ('+', '-', '*', '/')
operation_menu.current(0)
operation_menu.pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", font=('Arial', 12, 'bold'), bg="lightblue", command=calculate).pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result: ", font=('Arial', 14, 'bold'), bg="#f0f0f0")
label_result.pack(pady=10)

# Start GUI event loop
root.mainloop()
