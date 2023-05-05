import numpy as np
import cv2
import matplotlib.pyplot as plt

# def mnist_images_parser(image_path):
#     image_buffer = open(image_path).read()
#     magic_num,image_num,rows,columns = np.frombuffer(image_buffer,">i",4,0)
#     images = np.frombuffer(image_buffer,np.uint8,-1,16)
#     images = images.reshape(image_num,rows,columns)
#     assert magic_num== 2051,"Label parsing failed"
#     return images
# def mnist_labels_parser(label_path):
#     label_buffer = open(label_path).read()
#     magic_num,label_num= np.frombuffer(label_buffer,">i",2,0)
#     labels = np.frombuffer(label_buffer,np.uint8,-1,4)
#     assert magic_num== 2049,"Label parsing failed"
#     return labels


class Dataset:
    def __init__(self,images_path,label_path):
        self.image_path = images_path
        self.label_path = label_path
    def __len__(self):
        len_image = len(self.mnist_images_parser(self.image_path))
        len_label = len(self.mnist_labels_parser(self.label_path))
        assert len_label==len_image,"len of labels and images are different"
        return len_image
    def __getitem__(self, item):
        self.images = self.mnist_images_parser(self.image_path)
        self.labels = self.mnist_labels_parser(self.label_path)
        return self.images[item],self.labels[item]
    @staticmethod
    def mnist_images_parser(image_path):
        image_buffer = open(image_path,"rb").read()
        magic_num, image_num, rows, columns = np.frombuffer(image_buffer, ">i", 4, 0)
        images = np.frombuffer(image_buffer, np.uint8, -1, 16)
        images = images.reshape(image_num, rows, columns)
        assert magic_num == 2051, "Label parsing failed"
        return images

    @staticmethod
    def mnist_labels_parser(label_path):
        label_buffer = open(label_path,"rb").read()
        magic_num, label_num = np.frombuffer(label_buffer, ">i", 2, 0)
        labels = np.frombuffer(label_buffer, np.uint8, -1, 8)
        assert magic_num == 2049, "Label parsing failed"
        return labels

# class DataIteration:
#     def __init__(self,dataset,iter,batch):
#         self.dataset = dataset
#         self.iter = iter
#         self.batch = batch
#         self.cursor = 0
#     def __next__(self):
#         begin = self.cusor
#         end = self.cursor+ self.batch
#         if end>len(self.dataset):
#             self.cursor =0
#             raise StopIteration()

class DataLoader:
    def __init__(self,dataset,batch):
        self.dataset = dataset
        self.batch = batch
        self.cursor = 0
    def __iter__(self):
        self.indexes = list(range(len(self.dataset)))
        np.random.shuffle(self.indexes)
        return self
    def __next__(self):
        begin = self.cursor
        end = self.cursor + self.batch
        if end>len(self.dataset):
            self.cursor =0
            raise StopIteration()
        temp_batch = []
        for index in self.indexes[begin:end]:  #batch数据对应的是index数列，先找到index数列，再根据index找对应的数据
            item = self.dataset[index]
            temp_batch.append(item)
        # return list(zip(*temp_batch))
        self.cursor +=1
        return [np.stack(item,axis=0) for item in list(zip(*temp_batch))]






dataset = Dataset("mnist_data/t10k-images.idx3-ubyte","mnist_data/t10k-labels.idx1-ubyte")
print(len(dataset))
# image,label = dataset[0]
dataloader = DataLoader(dataset,5)
# print(len(dataset))
show_count = 0
for images,labels in dataloader:
    print(images.shape)
    print(labels.shape)
    plt.title(f"label is {labels[0]}")
    plt.imshow(images[0])
    plt.show()
    print("one circle is done")
    # break
# plt.title(f"label is {label}")
# plt.imshow(image)
# plt.show()


# image_buffer = open("mnist_data/t10k-images.idx3-ubyte","rb").read()
# label_buffer = open("mnist_data/t10k-labels.idx1-ubyte","rb").read()
#
# magic_num,image_num,row,column = np.frombuffer(image_buffer,">i",4,0)
# labels = (np.frombuffer(label_buffer,np.uint8,-1,8))
#
# images = np.frombuffer(image_buffer,np.uint8,-1,16)
# images = images.reshape(image_num,row,column)
# print(images[0])
# show_index = 10
# plt.title(f"label is {labels[show_index]}")
# plt.imshow(images[show_index])
# plt.show()
# cv2.imshow(f"{labels[0]}",images[0])
# cv2.waitKey(0)
# print(magic_num,image_num,row,column)

#1. 定义一个parser解析所有的label文件/image文件数据，两个函数分别解析  assert断言magic number
#2. 定义dataset，传入images和labels
#3. 定义dataloader，迭代器分开实现，zip(*batch_data),把标签和 图片分离分离；
#   进一步np.stack分别拼接图片和标签，各形成一个变量
#4. 采用for循环方法展示所有图片和标签
