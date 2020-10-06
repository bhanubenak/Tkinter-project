from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("born to shine!!")

root.filename = filedialog.askopenfilename(initialdir="C:\\Users\\Admin\\Desktop\\tkinter(freecodecamp)\\images\\",
                                           title="Select a file", filename=(("png files", "*.png"), ("all files", "*.*")))


mainloop()
