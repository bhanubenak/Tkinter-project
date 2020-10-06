from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("born to shine!!")
root.geometry("400x200")


def graph():
    house_prices = np.random.normal(20000, 25000, 5000)
    plt.hist(house_prices, 2 0)
    plt.show()


my_btn = Button(root, text="Graph it!", command=graph)
my_btn.grid()

root.mainloop()
