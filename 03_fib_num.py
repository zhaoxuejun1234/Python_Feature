import time
from collections.abc import Iterable
from collections.abc import Iterator
class Fib(object):
    def __init__(self):
        self.num1 =0
        self.num2 =1
    def __iter__(self):
        return self
    def __next__(self):
        temp = self.num1+self.num2
        self.num1 = self.num2
        self.num2 = temp
        return self.num1

def fib_num(a,b):
    num1,num2 =a,b
    def inner():
        nonlocal num1,num2
        num1,num2 = num2, num1+num2
        return num1
    return inner
#
func = fib_num(0,1)
fib = Fib()
print(isinstance(fib,Iterable),isinstance(fib,Iterator))
while True:
    # print(func())
    print(next(fib))
    time.sleep(1)

