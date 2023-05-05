import time

datalist = [6,7,8,9,110,10,220,30]
class Iterator():
    def __init__(self,datalist):
        self.data = datalist
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        # pass
        #基于迭代器实现数据遍历
        # if self.count < len(self.data):
        #     data = yield (self.data[self.count])
        #     self.conut+=1
        # else:
        #     self.count = 0
        #     raise StopIteration
        # return data

        #普通的数据遍历方法
        if self.count<len(self.data):
            data = (self.data[self.count])
            self.count += 1
        else:
            self.count = 0
            raise StopIteration
        return data

iter = Iterator(datalist)
print(type(iter))
for i in iter:
    print(i)
# while True:
#     try:
#         print(next(iter))
#         time.sleep(1)
#     except StopIteration as ret:
#         print("Iteration is done")
#         break


