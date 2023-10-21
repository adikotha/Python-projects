import tkinter as tk

def calculate_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())

    # Simple interest calculation
    simple_interest = (principal * rate * time) / 100

    # Compound interest calculation
    compound_interest = principal * (1 + rate/100)**time - principal

    simple_interest_label.config(text="Simple interest: $" + str(round(simple_interest, 2)))
    compound_interest_label.config(text="Compound interest: $" + str(round(compound_interest, 2)))

# Create a GUI window
window = tk.Tk()
window.title("Interest Calculator")

# Create entry fields for user input
principal_label = tk.Label(window, text="Enter principal amount:")
principal_label.pack()
principal_entry = tk.Entry(window)
principal_entry.pack()

rate_label = tk.Label(window, text="Enter interest rate (%):")
rate_label.pack()
rate_entry = tk.Entry(window)
rate_entry.pack()

time_label = tk.Label(window, text="Enter time period (years):")
time_label.pack()
time_entry = tk.Entry(window)
time_entry.pack()

# Create a button to calculate interest
calculate_button = tk.Button(window, text="Calculate", command=calculate_interest)
calculate_button.pack()

# Create labels to display results
simple_interest_label = tk.Label(window, text="")
simple_interest_label.pack()

compound_interest_label = tk.Label(window, text="")
compound_interest_label.pack()

# Start the GUI window
window.mainloop()
