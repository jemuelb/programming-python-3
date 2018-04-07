# callback handlers: reloaded each time triggered


def message1():
    print('just kidding')


def message2(self):
    print('blah blah blah')
    self.method1()
