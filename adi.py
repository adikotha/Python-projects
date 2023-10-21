import random
import string
import tkinter as tk
from tkinter import messagebox

# Define the main window
root = tk.Tk()
root.title("Password and OTP Generator")

# Define the font style for the labels and buttons
font_style = ("Arial", 12)

# Define the label and radio buttons for password and OTP generation
generate_label = tk.Label(root, text="Generate:", font=font_style)
generate_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

generate_var = tk.StringVar(value="Password")
generate_password = tk.Radiobutton(root, text="Password", variable=generate_var, value="Password", font=font_style)
generate_password.grid(row=1, column=0, padx=5, pady=5, sticky="w")

generate_otp = tk.Radiobutton(root, text="OTP", variable=generate_var, value="OTP", font=font_style)
generate_otp.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Define the label and entry box for password/OTP length
length_label = tk.Label(root, text="Length:", font=font_style)
length_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

length_entry = tk.Entry(root, width=10, font=font_style)
length_entry.insert(0, "8")
length_entry.grid(row=4, column=0, padx=5, pady=5, sticky="w")

# Define the button for password/OTP generation
generate_button = tk.Button(root, text="Generate", font=font_style, bg="lightblue", fg="black", width=15)

def generate_password(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "@_@_@_"
    
    # Make sure the password is at least 8 characters long
    if length < 8:
        length = 8
    
    # Generate a password with at least one uppercase letter, one lowercase letter, one digit, and one special character
    password = random.choice(uppercase) + random.choice(lowercase) + random.choice(digits) + random.choice(special)
    password += ''.join(random.choice(uppercase + lowercase + digits + special) for i in range(length - 4))
    
    # Shuffle the password to make it more random
    password = ''.join(random.sample(password, len(password)))
    
    messagebox.showinfo("Generated Password", password + "\n" + classify_password_strength(password))

def generate_otp(length):
    characters = string.digits
    otp = ''.join(random.choice(characters) for i in range(length))
    messagebox.showinfo("Generated OTP", otp)

# selection of otp or password
def generate():
    length = int(length_entry.get())
    if generate_var.get() == "Password":
        generate_password(length)
    elif generate_var.get() == "OTP":
        generate_otp(length)

generate_button.config(command=generate)
generate_button.grid(row=5, column=0, padx=5, pady=5, sticky="w")

# Define the label and text box for password strength classification
strength_label = tk.Label(root, text="Strength:", font=font_style)
strength_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

strength_text = tk.Text(root, height=1, width=20, font=font_style)
strength_text.insert(tk.END, "")
strength_text.config(state=tk.DISABLED)
strength
