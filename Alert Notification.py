# This is a simple application for alert system

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")
def message():
    messagebox.showwarning("Alert Box", "Stop virus found")
but = Button(root, text="ok", command=Message)
but.place(x=100, y=100)
root.mainloop()