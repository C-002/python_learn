import _thread
import time

def action(i):
    print(i ** 32)

class Power:
    def __init__(self, i):
        self.i = i
    def action(self):
        print(self.i ** 32)

#action(2)
_thread.start_new_thread(action, (2,))

_thread.start_new_thread((lambda: action(2)), ())

obj = Power(2)
_thread.start_new_thread(obj.action, ())

time.sleep(2)   #wait for end of threads

