from time import sleep
from threading import Thread


class Hello(Thread):

    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)


class Hi(Thread):

    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)


h = Hello()
hi = Hi()
h.start()
sleep(0.5)
hi.start()
h.join()
hi.join()
print('Bye')
