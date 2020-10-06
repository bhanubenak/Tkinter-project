from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Born To Shine!!")
root.geometry("300x300")


def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="check this box..!",
                variable=var, onvalue="ON", offvalue="Off")

c.deselect()
c.pack()


myButton = Button(root, text="show selection", command=show).pack()

root.mainloop()
