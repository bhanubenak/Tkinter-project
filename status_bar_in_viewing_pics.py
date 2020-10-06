

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Born to Shine")
# root.iconbitmap(bitmap=...)


my_img_1 = ImageTk.PhotoImage(Image.open(
    "C:\\Users\\Admin\\Desktop\\tkinter(freecodecamp)\\images\\lee_quote.png"))
my_img_2 = ImageTk.PhotoImage(Image.open(
    "C:\\Users\\Admin\\Desktop\\tkinter(freecodecamp)\\images\\me.png"))
my_img_3 = ImageTk.PhotoImage(Image.open(
    "C:\\Users\\Admin\\Desktop\\tkinter(freecodecamp)\\images\\greenland.png"))
my_img_4 = ImageTk.PhotoImage(Image.open(
    "C:\\Users\\Admin\\Desktop\\tkinter(freecodecamp)\\images\\lee_logo.png"))
my_img_5 = ImageTk.PhotoImage(Image.open(
    "C:\\Users\\Admin\\Desktop\\tkinter(freecodecamp)\\images\\sky.png"))
my_img_6 = ImageTk.PhotoImage(Image.open(
    "C:\\Users\\Admin\\Desktop\\tkinter(freecodecamp)\\images\\wide_angle.png"))

image_list = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5, my_img_6]

status = Label(root, text="Image 1 of " +
               str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


my_label = Label(image=my_img_1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 6:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image" + str(image_number) + "of" +
                   str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + "of" +
                   str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=S+E)

root.mainloop()
