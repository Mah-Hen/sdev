from threading import *

def f():
    while True:
        pass

t = Thread(target=f)
t.start()