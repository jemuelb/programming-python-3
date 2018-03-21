"""
show one image with PIL photo replacement object
handles many more image types; install PIL first
"""

import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage  # this replaces PhotoImage from tkinter

imgdir = '../../images'
imgfile = 'florida-2009-1.jpg'
if len(sys.argv) > 1:
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)
Label(win, image=imgobj).pack()
win.mainloop()
print(imgobj.width(), imgobj.height())

