"""
read command pipe in a thread and place output on a queue checked in timer loop;
allows script to display program's output without being blocked between its outputs;
spawned programs need not connect or flush, but this approaches complexity of sockets
"""

import _thread as thread, queue, os
from tkinter import Tk
from guiStreams import GuiOutput
stdoutQueue = queue.Queue()


def producer(input):
    while True:
        line = input.readline()
        stdoutQueue.put(line)
        if not line:
            break


def consumer(output, root, term='<end>'):
    try:
        line = stdoutQueue.get(block=False)
    except queue.Empty:
        pass
    else:  # executes if try succeeds
        if not line:
            output.write(term)
            return
        output.write(line)
    root.after(250, lambda: consumer(output, root, term))


def redirectedGuiShellCmd(command, root):
    input = os.popen(command, 'r')  # pipes shell command
    output = GuiOutput(root)  # redirects output to Tk window
    thread.start_new_thread(producer, (input,))  # output to queue
    consumer(output, root)  # tries to retrieve from queue


if __name__ == '__main__':
    win = Tk()
    redirectedGuiShellCmd('python3 -u pipe-nongui.py', win)
    win.mainloop()
