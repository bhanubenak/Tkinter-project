from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Born to Shine")
# root.iconbitmap(bitmap=...)

my_img = ImageTk.PhotoImage(Image.open(
    "C:\\Users\\Admin\\Desktop\\tkinter(freecodecamp)\\images\\me.png"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()
