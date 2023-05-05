import time
def timer(func):
    def wrapper(count,a,b):
        start = time.time()
        dot = func(count,a,b)
        end = time.time()
        span = end - start
        print(f"result is {dot} and time is {span*1000} ms")
        return dot
    return wrapper


# func = timer(computation)
# func(1000000,1,2)
# func(2000000,1,2)
# computation(100000,1,2)
# computation(200000,1,2)
# class Timer:
#     def __init__(self,name):
#         self.name = name
#     def __call__(self,func):
#         def wrapper(count,a,b):
#             start = time.time()
#             dot = func(count, a, b)
#             end = time.time()
#             span = end - start
#             print(f"{self.name} result is {dot} and time is {span * 1000} ms")
#             return dot
#         return wrapper
# @Timer("test")
# def computation(count,a,b):
#     sum  = 0
#     for i in range(count):
#          sum += a*b
#     return sum
# computation(100000,1,2)
# computation(200000,1,2)
import time
class Timer:
    def __init__(self,func):
        self.func = func
    def __call__(self,count,a,b):
        start = time.time()
        dot = self.func(count, a, b)
        end = time.time()
        span = end - start
        print(f" result is {dot} and time is {span * 1000} ms")
        return dot
@Timer
def computation(count,a,b):
    sum  = 0
    for i in range(count):
         sum += a*b
    return sum
computation(100000,1,2)
computation(200000,1,2)