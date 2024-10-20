import tkinter as tk
from tkinter import messagebox

# Function for performing calculations
def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return
        
        label_result.config(text=f"Result: {result}")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Main GUI code
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operation = tk.Label(root, text="Select operation:")
label_operation.grid(row=2, column=0, padx=10, pady=10)

# Dropdown for selecting operation
operation_var = tk.StringVar(root)
operation_var.set("Add")  # Default value

dropdown_operation = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
dropdown_operation.grid(row=2, column=1, padx=10, pady=10)

# Button to perform calculation
button_calculate = tk.Button(root, text="Calculate", command=perform_calculation)
button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display result
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
