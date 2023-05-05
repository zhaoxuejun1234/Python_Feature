import numpy as np
class dataset:
    def __init__(self,dataset):
        self.dataset = dataset
        self.cursor = 0
    def __len__(self):
        return len(self.dataset)
    def __getitem__(self,item):
        image,label = self.dataset[item]
        return image,label
    # def __iter__(self):
    #     return self
    # def __next__(self):
    #     if self.cursor<len(self.dataset):
    #         num = self.dataset[self.cursor]
    #         self.cursor +=1
    #     else:
    #         self.cursor=0
    #         raise StopIteration
    #     return num
class DataLoader:
    def __init__(self,data,batch):
        self.data = data.dataset
        self.batch = batch
        self.cursor = 0
    def __iter__(self):
        self.indexes = list(range(len(self.data)))
        np.random.shuffle(self.indexes)
        return self
    def __next__(self):
        begin = self.cursor
        end = self.cursor + self.batch
        if end <= len(self.data):
            batch_data = self.data[begin:end]
            self.cursor += self.batch
        else:
            self.cursor = 0
            raise StopIteration
        temp_batch = []
        for index in self.indexes[begin:end]:
            item = self.data[index]
            temp_batch.append(item)
        return temp_batch
#缝合dataset和 dataloader，没卵用
# class Monster:
#     def __init__(self,data,batch):
#         self.dataset = data
#         self.batch = batch
#         self.cursor = 0
#
#     def __len__(self):
#         return len(self.dataset)
#     def __getitem__(self, item):
#         image, label = self.dataset[item]
#         return image, label
#     def __iter__(self):
#         self.indexes = list(range(len(self.dataset)))
#         np.random.shuffle(self.indexes)
#         return self
#     def __next__(self):
#         begin = self.cursor
#         end = self.cursor + self.batch
#         if end <= len(self.dataset):
#             batch_data = self.dataset[begin:end]
#             self.cursor += self.batch
#         else:
#             self.cursor = 0
#             raise StopIteration()
#         temp_batch = []
#         for index in self.indexes[begin:end]:
#             # print(index)
#             item = self.dataset[index]
#             temp_batch.append(item)
#         return temp_batch
# images = [[f"images {i}",i] for i in range(10)]
# batch_size = 2
# monster = Monster(images,batch_size)
# for item in monster:
#     print(item)
# print(images)


# images = [[f"images {i}",i] for i in range(10)]
# batch_size = 2
# dataset = dataset(images)
# DataLoader = DataLoader(dataset,batch_size)
# for item in DataLoader:
#     print(item)

