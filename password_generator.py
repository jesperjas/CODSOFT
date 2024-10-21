import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a password
def generate_password():
    try:
        # Get the desired length from the user
        length = int(entry_length.get())

        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return

        # Characters for the password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the generated password
        label_password.config(text=f"Generated Password: {password}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label for password length
label_length = tk.Label(root, text="Enter the desired length for the password:")
label_length.grid(row=0, column=0, padx=10, pady=10)

# Entry to take password length input
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Button to generate password
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.grid(row=1, column=0, columnspan=2, pady=10)

# Label to display the generated password
label_password = tk.Label(root, text="Generated Password: ")
label_password.grid(row=2, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()

