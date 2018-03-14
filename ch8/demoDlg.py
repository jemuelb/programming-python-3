"create a bar of simple buttons that launch dialog demos"

from tkinter import *
from dialogTable import demos
from quitter import Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Basic demos").pack()  # label on top of window
        for (key, value) in demos.items():  # builds the list of buttons from 'demos'
            Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)  # separate quit button from import


if __name__ == '__main__':
    Demo().mainloop()
