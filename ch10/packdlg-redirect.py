# wrap command-line script in GUI redirection tool to popup its output

from tkinter import *
from packdlg import runPackDialog
from guiStreams import redirectedGuiFunc


def runPackDialog_Wrapped():
    redirectedGuiFunc(runPackDialog)


if __name__ == '__main__':
    root = Tk()
    Button(root, text='pop', command=runPackDialog_Wrapped).pack(fill=X)
    root.mainloop()
