from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Born to shine!!")


def open():
    global my_img
    top = Toplevel()
    top.title("my second Window")
    my_img = ImageTk.PhotoImage(Image.open(
        "C:\\Users\\Admin\\Desktop\\tkinter(freecodecamp)\\images\\lee_quote.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()
