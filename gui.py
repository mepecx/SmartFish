# import tkinter
import tkinter as tk
from tkinter import ttk


gui = tk.Tk()
gui.title("SmartFish")
gui.geometry("500x500")
tabControl = ttk.Notebook(gui)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")
tabControl.pack(expand=1, fill="both")

ttk.Label(tab1, text="SmartFish stuff").grid(column=0, row=0, padx=30, pady=30)


gui.mainloop()