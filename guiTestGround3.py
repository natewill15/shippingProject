import tkinter as tk
from tkinter import ttk
import pandas as pd
import funcs as fn

# get data from Excel file and create dataframes
input_data = "input.xlsx"
open_orders = pd.read_excel(input_data, sheet_name="OO")
inventory = pd.read_excel(input_data, sheet_name="INV")

# Remove unwanted columns
columns_to_delete = []  # put column names in this list
open_orders.drop(columns_to_delete, axis=1, inplace=True)

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

    is_window_open = None

    # if not is_window_open:

    def open_inv_button(self):
        if not 'normal' == self.parent.InventoryScreen.tk.Toplevel.state(self):
            self.newWindow = InventoryScreen(self)
        # self.app = InventoryScreen(self.newWindow)

    def enable_button(self):
        if 'normal' == tk.Toplevel.state():
            self.nav_button1.config(state="disabled")
        else:
            self.nav_button1.config(state="normal")


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

        self.main_label.grid(column=0, row=0)


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


inv = None


class InventoryScreen(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        global inv

        self.statusbar = Statusbar(self)
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        self.main = Main(self)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)

        self.navbar.nav_button1.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1500x600")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
