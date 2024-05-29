import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    return strength

# Function to display password strength
def display_strength():
    password = password_entry.get()
    strength = check_password_strength(password)
    
    if strength == 0:
        result_label.config(text="Password is too short", fg="red")
    elif strength == 1:
        result_label.config(text="Very Weak", fg="red")
    elif strength == 2:
        result_label.config(text="Weak", fg="orange")
    elif strength == 3:
        result_label.config(text="Moderate", fg="yellow")
    elif strength == 4:
        result_label.config(text="Strong", fg="blue")
    else:
        result_label.config(text="Very Strong", fg="green")

# Function to toggle password visibility
def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Setting up the GUI window
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("450x350")
window.configure(bg="#f0f0f0")

# Creating and placing widgets with enhanced UI
title_label = tk.Label(window, text="Password Strength Checker", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

frame = tk.Frame(window, bg="#ffffff", padx=20, pady=20, relief="groove", bd=2)
frame.pack(pady=10)

instruction_label = tk.Label(frame, text="Enter your password:", font=("Helvetica", 12), bg="#ffffff")
instruction_label.pack(pady=5)

password_entry = tk.Entry(frame, show="*", width=30, font=("Helvetica", 12), relief="solid", bd=1)
password_entry.pack(pady=10)

# Adding the toggle password visibility checkbutton
show_password_var = tk.BooleanVar()
show_password_checkbutton = tk.Checkbutton(frame, text="Show Password", font=("Helvetica", 10), bg="#ffffff", variable=show_password_var, command=toggle_password)
show_password_checkbutton.pack(pady=5)

check_button = tk.Button(frame, text="Check Strength", font=("Helvetica", 12, "bold"), bg="#4caf50", fg="#ffffff", relief="raised", command=display_strength)
check_button.pack(pady=10)

result_label = tk.Label(frame, text="", font=("Helvetica", 12, "bold"), bg="#ffffff")
result_label.pack(pady=10)

# Running the main loop
window.mainloop()
