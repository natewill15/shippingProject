# Shipping/Reserving Process Improvement
# Nathan Williamson
#

import pandas as pd
import tkinter as tk

data = [
    {"SO": 1, "Customer": "Joe", "Quantity": 35},
    {"SO": 2, "Customer": "Billy", "Quantity": 60}
]

df = pd.DataFrame(data)

# GUI
root = tk.Tk()
root.title("My GUI Application")

# Set the size of the window (width x height)
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Allow resizing in both directions
root.resizable(True, True)

# Create an outer frame to hold the widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)    # Adding some padding for better appearance

# Widgets
label = tk.Label(frame, text="Hello, Tkinter!")
button = tk.Button(frame, text="Click Me")
entry = tk.Entry(frame)

# Pack
label.grid(row=0, column=0, sticky="nsew")
button.grid(row=2, column=0, sticky="nsew")
entry.grid(row=1, column=0, sticky="nsew")

# Configuring resizing behavior of the outer frame
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

# Center the frame within the window
root.update_idletasks()  # Update widget sizes before calculating
x_offset = (root.winfo_width() - frame.winfo_width()) // 2
y_offset = (root.winfo_height() - frame.winfo_height()) // 2
root.geometry(f"+{x_offset}+{y_offset}")  # Set window position

# Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


root.mainloop()
