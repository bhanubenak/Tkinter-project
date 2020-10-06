from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("born to shine!!")

frame = LabelFrame(root, padx=30, pady=30)
frame.pack(padx=10, pady=10)

b = Button(frame, text="dont click here!")
b2 = Button(frame, text="... or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()
