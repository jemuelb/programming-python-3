gifdir = '../../gifs/'  # gifs folder is two folders above current

from tkinter import *

win = Tk()
igm = PhotoImage(file=gifdir + "ora-pp.gif")
Button(win, image=igm).pack()
win.mainloop()
