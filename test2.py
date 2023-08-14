import tkinter as tk
from tkinter import ttk
import os
import socket
import pandas as pd

# Read data from an Excel file and create a DataFrame
excel_file_path = "your_file.xlsx"  # Replace with the path to your Excel file
open_orders = pd.read_excel("input.xlsx", sheet_name="OO")
inventory = pd.read_excel("input.xlsx", sheet_name="INV")

# GUI
root = tk.Tk()
root.title("My GUI Application")

# Set the size of the window (width x height)
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

df_list = list(open_orders.columns)

# Create a horizontal scrollbar
x_scrollbar = ttk.Scrollbar(root, orient=tk.HORIZONTAL)
x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

df_tree = ttk.Treeview(root, columns=df_list, show='headings', xscrollcommand=x_scrollbar.set)


# Set column headings for tree
def set_column_headings(tree, df):
    for idx, col in enumerate(open_orders.columns):
        tree.heading(idx, text=col)
        tree.column(idx, width=100)


set_column_headings(df_tree, open_orders)

# Connect the horizontal scrollbar to the Treeview
x_scrollbar.config(command=df_tree.xview)

df_tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == '__main__':
    root.mainloop()
