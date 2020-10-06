from tkinter import *

root = Tk()

# e = Entry(root, width=20, fg="red", bg="orange", borderwidth=9)
e = Entry(root, width=20)
e.pack()
e.insert(0, "enter ur name: ")


def myclick():
    hello = "hello" + e.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()


myButtom = Button(root, text="enter your name", command=myclick)
myButtom.pack()


root.mainloop()
