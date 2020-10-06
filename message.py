from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("bron to shine!!")


def popup():
    response = messagebox.askokcancel("this is popup", "Hello world")
    Label(root, text=response).pack()
    if response == "yes":
        Label(root, text="you clicked Yes!").pack()
    else:
        Label(root, text="you clicked No!").pack()


Button(root, text="popup", command=popup).pack()


mainloop()
