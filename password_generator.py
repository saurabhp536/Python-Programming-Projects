import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def toggle_visibility():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and pack widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_visibility)
show_password_checkbox.pack()

# Run the main loop
root.mainloop()
