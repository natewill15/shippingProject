import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import simpledialog

# ----------------------------------------------------------------------------------------------------------------------
# Import Excel data
# ----------------------------------------------------------------------------------------------------------------------
open_orders = pd.read_excel("input.xlsx", sheet_name="OO")
inventory = pd.read_excel("input.xlsx", sheet_name="INV")

# Delete unwanted columns
columns_to_delete = []  # Insert column names here to delete
open_orders.drop(columns_to_delete, axis=1, inplace=True)

open_orders_columns = list(open_orders.columns)  # used to create tree view

trucks = {
    'Name': []
}



# ----------------------------------------------------------------------------------------------------------------------
# End Import Excel data
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Main window
# ----------------------------------------------------------------------------------------------------------------------

class Navbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.open_inv_button = None
        self.parent = parent

        # Create and layout widgets for navbar

        self.navbar_label = tk.Label(self, text="THIS IS THE NAVBAR")
        self.open_inv_button = tk.Button(self, text="View Inventory", relief="raised", command=self.inv_button_click)
        self.button2 = tk.Button(self, text="Button 2", relief="raised", command=self.button2_click)
        self.button3 = tk.Button(self, text="Button 3", relief="raised", command=self.button3_click)
        self.button4 = tk.Button(self, text="Button 4", relief="raised", command=self.button4_click)

        self.navbar_label.pack(padx=2, pady=4, fill=tk.X)
        self.open_inv_button.pack(padx=2, pady=4, fill=tk.X)
        self.button2.pack(padx=2, pady=4, fill=tk.X)
        self.button3.pack(padx=2, pady=4, fill=tk.X)
        self.button4.pack(padx=2, pady=4, fill=tk.X)

    # Commands for Navbar buttons

    def inv_button_click(self):
        print("You clicked 'View Inventory'")

    def button2_click(self):
        print("You clicked Button 2")

    def button3_click(self):
        print("You clicked Button 3")

    def button4_click(self):
        print("You clicked Button 4")


class Toolbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.entry = tk.Entry(self)

        # Create and layout widgets for the toolbar
        self.toolbar_label = tk.Label(self, text="THIS IS THE TOOLBAR")
        self.add_truck_button = tk.Button(self, text="Add Truck", command=self.add_truck_click)

        self.toolbar_label.pack(side="left", pady=2, padx=2)
        self.add_truck_button.pack(side="left", pady=2, padx=2)
        self.entry.pack(side="left")

        # Create cascade menu
        # self.create_cascading_menu()

    def add_truck_click(self):
        truck_name = self.entry.get()
        if self.entry is None or truck_name == "":
            pass
        else:
            # Add to list and listbox
            self.parent.truck.truck_list.append(truck_name)
            self.parent.truck.truck_listbox.insert(tk.END, truck_name)
            self.entry.delete(0, tk.END)
            # create class
            Truck(self.entry, None)
            print(self.parent.truck.truck_list)
            print(Truck)
            print("click")

    def file_new(self):
        print("New File")

    def file_open(self):
        print("Open File")

    def edit_cut(self):
        print("Cut")

    def edit_copy(self):
        print("Copy")

    def edit_paste(self):
        print("Paste")


class Statusbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create and layout widgets for the statusbar

        self.statusbar_label = tk.Label(self, text="THIS IS THE STATUSBAR")

        self.statusbar_label.pack(pady=2)


# Creating truck list frame

class TruckListFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.truck_list = []

        self.truck_label = tk.Label(self, text="Truck List:")
        self.truck_listbox = tk.Listbox(self, )

        self.truck_label.pack(padx=2, pady=4, fill=tk.X)
        self.truck_listbox.pack(fill=tk.BOTH, expand=True, pady=2, padx=2)



# Creating tree view for window 1 main area
# ----------------------------------------------------------------------------------------------------------------------

class TreeFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.open_orders = open_orders
        self.open_orders_columns = open_orders_columns

        # Create scrollbars for the treeview
        x_scrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        y_scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)

        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(self, columns=open_orders_columns, show='headings', xscrollcommand=x_scrollbar.set,
                                 yscrollcommand=y_scrollbar.set)

        # Connect scrollbars to tree view
        x_scrollbar.config(command=self.tree.xview)
        y_scrollbar.config(command=self.tree.yview)

        def set_column_headings(tree, df):
            for idx, col in enumerate(df.columns):
                # print(idx)
                # print(col)
                self.tree.heading(idx, text=col)
                self.tree.column(idx, width=200)

        set_column_headings(self.tree, self.open_orders)

        # Create the col_mapping dictionary before using it
        col_mapping = {idx: col for idx, col in enumerate(open_orders.columns)}

        # Insert data from the Dataframe
        for index, row in open_orders.iterrows():
            values = [row[col_mapping[idx]] for idx in range(len(open_orders.columns))]
            self.tree.insert('', 'end', values=values)

        self.tree.pack(fill="both", expand=True)


class MainArea(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create and layout widgets for the statusbar

        self.main_area_label = tk.Label(self, text="THIS IS THE MAIN AREA", relief='solid', borderwidth=1)
        self.tree = TreeFrame(self)

        self.main_area_label.pack(side="top", fill='both', expand=False, padx=4, pady=4)
        self.tree.pack(side="top", fill="both", expand=True, padx=4, pady=4)


# Window with widgets from above


class Window1(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create widgets
        self.statusbar = Statusbar(self, relief="solid", borderwidth=1, background="grey")
        self.toolbar = Toolbar(self, relief="solid", borderwidth=1, background="grey")
        self.navbar = Navbar(self, relief="solid", borderwidth=1, background="grey")
        self.main = MainArea(self, relief="solid", borderwidth=1, background="grey")
        self.truck = TruckListFrame(self, relief="solid", borderwidth=1, background="grey")

        # Configure rows and columns
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=0)
        # self.columnconfigure(2, weight=0)

        self.statusbar.pack(side="bottom", fill="x", pady=(5, 0))
        self.toolbar.pack(side="top", fill="x", pady=(0, 5))
        self.navbar.pack(side="left", fill="y", pady=(5, 5), padx=(0, 5))
        self.truck.pack(side="right", fill='y', expand=True, pady=(5, 5), padx=(5, 0))
        self.main.pack(side="left", fill="both", expand=True, pady=(5, 5), padx=(5, 5))

        self.create_cascading_menu()

    def create_cascading_menu(self):
        menu_bar = tk.Menu(self.parent)
        self.parent.config(menu=menu_bar)

        # functions are in toolbar class for some reason

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.toolbar.file_new)
        file_menu.add_command(label="Open", command=self.toolbar.file_open)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.parent.quit)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.toolbar.edit_cut)
        edit_menu.add_command(label="Copy", command=self.toolbar.edit_copy)
        edit_menu.add_command(label="Paste", command=self.toolbar.edit_paste)


# ----------------------------------------------------------------------------------------------------------------------
# End main window
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# 2nd window
# ----------------------------------------------------------------------------------------------------------------------

class Window2(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class Truck:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.load = {}
        for key in open_orders_columns:
            self.load[key] = None

class Load(Truck):
    def __init__(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1500x600")
    root.title("Shipping Project")
    Window1(root).pack(side="top", fill="both", expand=True, padx=10, pady=10)
    root.mainloop()
