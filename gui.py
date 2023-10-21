import random
import string
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Password and OTP Generator")

# main screen
generate_label = tk.Label(root, text="Generate:")
generate_var = tk.StringVar(value="Password")
generate_password = tk.Radiobutton(root, text="Password", variable=generate_var, value="Password")
generate_otp = tk.Radiobutton(root, text="OTP", variable=generate_var, value="OTP")
length_label = tk.Label(root, text="Length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate")

generate_label.pack()
generate_password.pack()
generate_otp.pack()
length_label.pack()
length_entry.pack()
generate_button.pack()

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
    
    messagebox.showinfo("Generated Password", password)

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
root.mainloop()
