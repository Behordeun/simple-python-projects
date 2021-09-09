from pdb import Restart
from tkinter import * 
from tkinter import messagebox
import os

root = Tk()
root.geometry("300x300")
def shut():
    os.system("shutdown /s")
ttk = Button(root, text="SHUT DOWN", command=shut).pack()

def restart():
    os.system("shutdown /r")
ttk1 = Button(root, text="RESTART", command=shut).pack()

def sleep():
    os.system("shutdown /l")
ttk3 = Button(root, text="SLEEP", command=shut).pack()

def hibernate():
    os.system("shutdown /h")
ttk4 = Button(root, text="HIBERNATE", command=shut).pack()
root.mainloop()