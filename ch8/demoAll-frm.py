"""
4 demo class components (subframes) on one window;
there are 5 Quitter buttons on this one window too, and each kills entire gui;
GUIs can be reused as frames in container, independent windows, or processes;
"""

from tkinter import *
from quitter import Quitter
demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []


def addComponents(root):
    for demo in demoModules:  # demo is a class
        module = __import__(demo)  # imports the files from demoModule
        part = module.Demo(root)  # creates an instance of the class from import, this creates widget
        part.config(bd=2, relief=GROOVE)
        part.pack(side=LEFT, expand=YES, fill=BOTH)
        parts.append(part)  # appending the widget so state can be called later


def dumpState():
    for part in parts:
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')


root = Tk()
root.title('Frames')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()
