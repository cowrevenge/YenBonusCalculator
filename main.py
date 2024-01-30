import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

def calculate_values():
    try:
        agreed_value_usd = float(agreed_value_entry.get())
        current_exchange_rate = float(current_exchange_rate_entry.get())
        current_paid_value_jpy = float(current_paid_value_entry.get())
        new_rate = 0.0075

        current_value_usd = current_paid_value_jpy * current_exchange_rate
        adjusted_value_jpy = agreed_value_usd / new_rate
        bonus_jpy = (agreed_value_usd / current_exchange_rate) - current_paid_value_jpy

        current_value_usd_label.config(text=f"Current Value in USD: {current_value_usd:.2f}")
        adjusted_value_label.config(text=f"Adjusted Value in JPY: {adjusted_value_jpy:.2f}")
        bonus_label.config(text=f"Calculated Bonus in JPY: {bonus_jpy:.2f}")
    except ValueError:
        current_value_usd_label.config(text="Invalid input")
        adjusted_value_label.config(text="")
        bonus_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Define fonts
default_font = Font(family="Helvetica", size=10)
large_font = Font(family="Helvetica", size=20)  # Double the size for bonus

# Create widgets
agreed_value_label = ttk.Label(root, text="Agreed Value in USD:")
agreed_value_entry = ttk.Entry(root)
agreed_value_entry.insert(0, "4687.5")  # Default value

current_exchange_rate_label = ttk.Label(root, text="Current Exchange Rate:")
current_exchange_rate_entry = ttk.Entry(root)
current_exchange_rate_entry.insert(0, "0.0068")  # Default value

current_paid_value_label = ttk.Label(root, text="Current Paid Value in Yen:")
current_paid_value_entry = ttk.Entry(root)
current_paid_value_entry.insert(0, "625000")  # Default value

calculate_button = ttk.Button(root, text="Calculate", command=calculate_values)

current_value_usd_label = ttk.Label(root, text="Current Value in USD:")
adjusted_value_label = ttk.Label(root, text="Adjusted Value in JPY:")
bonus_label = ttk.Label(root, text="Calculated Bonus in JPY:", font=large_font)  # Larger font for bonus

# Arrange the widgets
agreed_value_label.pack()
agreed_value_entry.pack()

current_exchange_rate_label.pack()
current_exchange_rate_entry.pack()

current_paid_value_label.pack()
current_paid_value_entry.pack()

calculate_button.pack()

current_value_usd_label.pack()
adjusted_value_label.pack()
bonus_label.pack()

# Start the GUI event loop
root.mainloop()
