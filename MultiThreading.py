from time import sleep
from threading import *


class Hello(Thread):

    def run(self):
        for i in range(5):
            print('Hello', end=' ')
            sleep(0.5)


class Hi(Thread):

    def run(self):
        for i in range(5):
            print('Hi')
            sleep(0.5)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print('Bye')
