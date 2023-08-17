import tkinter as tk
from tkinter import ttk
import pandas as pd

# get data from Excel file and create dataframes
input_data = "input.xlsx"
open_orders = pd.read_excel(input_data, sheet_name="OO")
inventory = pd.read_excel(input_data, sheet_name="INV")

# Remove unwanted columns
columns_to_delete = []  # put column names in this list
open_orders.drop(columns_to_delete, axis=1, inplace=True)
