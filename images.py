from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Born to Shine")
# root.iconbitmap(bitmap=...)

my_img = ImageTk.PhotoImage(Image.open("IMG_20200312_180939148~2.jpg"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()
