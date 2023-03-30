from tkinter import *
from tkinter import ttk
def set_entry(*args):
    entry_1_txt.set("Hello")
def chk_but_changed(*args):
    entry_1_txt.set(chk_but_1_txt.get())
def radio_changed(*args):
    entry_1_txt.set(entry_but_1_val.get())
def combo_changed(*args):
    entry_1_txt.set(combo_1_val.get())
root=Tk()
root.title("Widget Example")

