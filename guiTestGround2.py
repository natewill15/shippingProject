import tkinter as tk
from tkinter import ttk
import os
import socket
import pandas as pd

# Read data from an Excel file and create a DataFrame
excel_file_path = "your_file.xlsx"  # Replace with the path to your Excel file
open_orders = pd.read_excel("input.xlsx", sheet_name="OO")
inventory = pd.read_excel("input.xlsx", sheet_name="INV")

# Delete unwanted columns
columns_to_delete = ["Price", "Extension", "Ship Date", "quantityreserved", "Job Summary for Sales", "soquant",
                     "Axiom PO1", "Old ID", "Shipped", "Serial", "qtyatrisk", "Order Type", "pickquant", "Reorder2",
                     "Carbon $"]
for i in columns_to_delete:
    open_orders.drop(i, axis=1, inplace=True)

df_list = list(open_orders.columns)


class Button(tk.Button):
    def __init__(self, parent, text, command=None, *args, **kwargs):
        tk.Button.__init__(self, parent, text=text, command=command, *args, **kwargs)
        self.parent = parent
        self.configure(relief=tk.RAISED, padx=10, pady=5)  # Customize button appearance


class Navbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.app = None
        self.newWindow = None
        self.parent = parent
        self.Button = Button

        # Create and layout your navbar widgets here

        self.navbar_label = tk.Label(self, text="Navbar")
        self.navbar_label.pack()

        self.nav_button1 = self.Button(self, text="View Inventory", command=self.open_inv_button)
        self.nav_button1.pack(padx=10)

    def open_inv_button(self):
        self.newWindow = tk.Toplevel(self.parent)
        self.app = InventoryScreen(self.newWindow)


class Toolbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create and layout your toolbar widgets here

        toolbar_label = tk.Label(self, text="Toolbar")
        toolbar_label.pack()


def refresh_button_click():
    print("data refreshed")


class Statusbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.set = args

        # Create and layout your statusbar widgets here

        self.status_label = tk.Label(self, text="Status: Ready")
        self.status_label.pack(side="left")

        self.alt_label = tk.Label(self, text="INFO", width=100, anchor='w')
        self.alt_label.pack(side='left')

        self.button = Button(self, text="Refresh", command=refresh_button_click)
        self.button.pack(side="left")

    def set_info_label(self, info):
        self.alt_label.config(text=info)


class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create and layout your main widgets here

        self.label_frame = tk.Frame(self)
        self.label_frame.pack(side='top', fill='x', expand=False)

        self.main_label = tk.Label(self.label_frame, text="Main Area")
        self.inv_label = tk.Label(self.label_frame, text="Inventory Info")

        less_than_or_equal_to = '\u2264'
        greater_than_or_equal_to = '\u2265'
        self.range_label1 = tk.Label(self.label_frame, text="x < 18'" + "\nbottom text", relief="solid", borderwidth=1, width=15)
        self.range_label2 = tk.Label(self.label_frame, text="18' " + less_than_or_equal_to + " x " + "< 20'" + "\nbottom text", relief="solid", borderwidth=1, width=15)
        self.range_label3 = tk.Label(self.label_frame, text="20' " + less_than_or_equal_to + " x " + "< 21'" + "\nbottom text", relief="solid", borderwidth=1, width=15)
        self.range_label4 = tk.Label(self.label_frame, text="21' " + less_than_or_equal_to + " x " + "< 22'" + "\nbottom text", relief="solid", borderwidth=1, width=15)
        self.range_label5 = tk.Label(self.label_frame, text="22' " + less_than_or_equal_to + " x " + "< 24'" + "\nbottom text", relief="solid", borderwidth=1, width=15)
        self.range_label6 = tk.Label(self.label_frame, text="24' " + less_than_or_equal_to + " x " + "< 36'" + "\nbottom text", relief="solid", borderwidth=1, width=15)
        self.range_label7 = tk.Label(self.label_frame, text="36' " + less_than_or_equal_to + " x " + "< 42'" + "\nbottom text", relief="solid", borderwidth=1, width=15)
        self.range_label8 = tk.Label(self.label_frame, text="42' " + greater_than_or_equal_to + " x " + "\nbottom text", relief="solid", borderwidth=1, width=15)

        #self.main_label.pack(side='left', padx=(20, 10), pady=10)
        #self.inv_label.pack(side='left', padx=(10, 20), pady=10)

        self.main_label.grid(column=0, row=0)
        self.inv_label.grid(column=1, row=0)
        self.range_label1.grid(column=2, row=0)
        self.range_label2.grid(column=3, row=0)
        self.range_label3.grid(column=4, row=0)
        self.range_label4.grid(column=5, row=0)
        self.range_label5.grid(column=6, row=0)
        self.range_label6.grid(column=7, row=0)
        self.range_label7.grid(column=8, row=0)
        self.range_label8.grid(column=9, row=0)

        # Create a horizontal scrollbar
        x_scrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X, padx=20)

        # Create a vertical scrollbar
        y_scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        df_tree = ttk.Treeview(self, columns=df_list, show='headings', xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)

        # Connect the horizontal scrollbar to the Treeview
        x_scrollbar.config(command=df_tree.xview)
        y_scrollbar.config(command=df_tree.yview)

        # Set column headings for tree
        def set_column_headings(tree, df):
            for idx, col in enumerate(open_orders.columns):
                tree.heading(idx, text=col)
                tree.column(idx, width=200)

        set_column_headings(df_tree, open_orders)



        # Create the col_mapping dictionary before using it
        col_mapping = {idx: col for idx, col in enumerate(open_orders.columns)}

        # Insert data from the DataFrame
        for index, row in open_orders.iterrows():
            values = [row[col_mapping[idx]] for idx in range(len(open_orders.columns))]
            df_tree.insert('', 'end', values=values)

        df_tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20)

        def select_item(a):

            cur_item = df_tree.focus()
            tree_selection_desc = df_tree.item(cur_item)['values'][5]
            filtered_orders = open_orders[open_orders['Description'] == tree_selection_desc]
            sum_filtered_orders = filtered_orders['Ordered'].sum()
            filtered_inv = inventory[inventory['description'] == tree_selection_desc]
            sum_filtered_inv = filtered_inv['fg'].sum()

            info = "Description: " + tree_selection_desc + "    " + "Ordered: " + str(
                '{:,}'.format(round(sum_filtered_orders, 2))) + "    " + "FG: " + str(
                '{:,}'.format(round(sum_filtered_inv, 2)))

            info2 = str('{:,}'.format(round(sum_filtered_inv, 2)))

            self.parent.statusbar.set_info_label(info)

            filter1 = filtered_inv[filtered_inv['fg'] < 18]
            filter2 = filtered_inv[(filtered_inv['fg'] >= 18) & (filtered_inv['fg'] < 20)]
            filter3 = filtered_inv[(filtered_inv['fg'] >= 20) & (filtered_inv['fg'] < 21)]
            filter4 = filtered_inv[(filtered_inv['fg'] >= 21) & (filtered_inv['fg'] < 22)]
            filter5 = filtered_inv[(filtered_inv['fg'] >= 22) & (filtered_inv['fg'] < 24)]
            filter6 = filtered_inv[(filtered_inv['fg'] >= 24) & (filtered_inv['fg'] < 36)]
            filter7 = filtered_inv[(filtered_inv['fg'] >= 36) & (filtered_inv['fg'] < 42)]
            filter8 = filtered_inv[filtered_inv['fg'] >= 42]




            # create dict for length ranges
            length_ranges = {"group1": str('{:,}'.format(round(filter1['fg'].sum(), 2))),
                             "group2": str('{:,}'.format(round(filter2['fg'].sum(), 2))),
                             "group3": str('{:,}'.format(round(filter3['fg'].sum(), 2))),
                             "group4": str('{:,}'.format(round(filter4['fg'].sum(), 2))),
                             "group5": str('{:,}'.format(round(filter5['fg'].sum(), 2))),
                             "group6": str('{:,}'.format(round(filter6['fg'].sum(), 2))),
                             "group7": str('{:,}'.format(round(filter7['fg'].sum(), 2))),
                             "group8": str('{:,}'.format(round(filter8['fg'].sum(), 2)))}

            self.set_inv_label(info2)
            self.set_range_labels(length_ranges)

            return info

        df_tree.bind('<ButtonRelease-1>', select_item)

    def set_inv_label(self, info):
        self.inv_label.config(text=info)

    def set_range_labels(self, info):
        self.range_label1.config(text="x < 18'" + "\n" + info['group1'])
        self.range_label2.config(text="18' " + "\u2264" + " x " + "< 20'" + "\n" + info['group2'])
        self.range_label3.config(text="20' " + "\u2264" + " x " + "< 21'" + "\n" + info['group3'])
        self.range_label4.config(text="21' " + "\u2264" + " x " + "< 22'" + "\n" + info['group4'])
        self.range_label5.config(text="22' " + "\u2264" + " x " + "< 24'" + "\n" + info['group5'])
        self.range_label6.config(text="24' " + "\u2264" + " x " + "< 36'" + "\n" + info['group6'])
        self.range_label7.config(text="36' " + "\u2264" + " x " + "< 42'" + "\n" + info['group7'])
        self.range_label8.config(text="x \u2265 42'" + "\n" + info['group8'])


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.statusbar = Statusbar(self)
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)

        # self.navbar.Button(parent, "View Inventory")

        self.main = Main(self)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)


class InventoryScreen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.statusbar = Statusbar(self)
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        self.main = Main(self)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1500x600")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
