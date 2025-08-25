import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")
        return

    operation = operation_var.get()
    if operation == 'Addition':
        result = num1 + num2
    elif operation == 'Subtraction':
        result = num1 - num2
    elif operation == 'Multiplication':
        result = num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            result = num1 / num2
        else:
            messagebox.showerror("Math Error", "Cannot divide by zero!")
            return
    else:
        messagebox.showerror("Invalid Operation", "Please select a valid operation!")
        return

    result_label.config(text=f"Result: {result}")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Labels and entries for numbers
tk.Label(root, text="First Number:").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text="Second Number:").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Operation selection
operation_var = tk.StringVar(value="Addition")
tk.Label(root, text="Select Operation:").pack(pady=5)
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack(pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate, bg="green", fg="white")
calc_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
