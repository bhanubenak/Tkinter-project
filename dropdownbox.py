from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("BORN TO SHINE!!")


def show():
    mylbl = Label(root, text=clicked.get()).pack()


options = [
    "Sunday", "Monday", "Tuesday",
    "Wednesday", "Thusday", "Friday", "Saturday"

]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

mybtn = Button(root, text="show selection", command=show).pack()
root.mainloop()


3, 23
