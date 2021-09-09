from tkinter import *
window = Tk()

label = Label(window, text = "To-Do-List")
label.pack()

list = Listbox(window, bg="yellow")
list.insert(1, "Wake up in the morning")
list.insert(2, "brush your teeth")
list.insert(3, "Take your bath")
list.insert(4, "Comb your hair")
list.insert(5, "Put on your cloth")
list.pack()
window.config(bg="black")
window.geometry("300x300")
window.title("To-Do List")
window.mainloop()
