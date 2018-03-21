from tkinter import *
from glob import glob
import demoCheck
import random

gifdir = '../../gifs/'


def draw():
    name, photo = random.choice(images)  # global var 'images', loaded in pictures below
    lbl.config(text=name)
    pix.config(image=photo)


root = Tk()
lbl = Label(root, text="none", bg='blue', fg='white')
pix = Button(root, text="Press me", command=draw, bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=100)  # pads out distance in y-axis
demoCheck.Demo(root, relief=SUNKEN, bd=2).pack(fill=BOTH)

files=glob(gifdir + "*.gif")
images = [(x, PhotoImage(file=x)) for x in files]
print(files)
root.mainloop()
