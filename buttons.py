from tkinter import *

root = Tk()


def myclick():
    mylabel = Label(root, text="!Loops Like You Clicked Button!")
    mylabel.pack()


# myButtom = Button(root, text="Clicks ME!!", state=DISABLED)
myButtom = Button(root, text="Clicks ME!!",
                  command=myclick, fg="red", bg="blue")

myButtom.pack()


root.mainloop()
