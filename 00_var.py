#regionstring
str ="hello world"
print(str[str.find("world")])
print(str[1:4:1])
print(str[-1::-1])
# print(str.__dir__())
# a =(1,"heelo",3.0)
# print(a[0])
print(str[slice(1,5,1)])
#endregion
#regiondict
#dic 增删查改，检索
dict3={}
dict1 = {"xuejun":"BJ000"}
dict2 = {"jingyi":"BJ001"}
dict3.update(dict1)
dict3.update(dict2)
dict3["xiaoming"]="BJ002"
# del dict3["xiaoming"]
dict3["xuejun"]
dict3.get("xuejun")
#返回并弹出最后一个键值对
dict3.popitem()
#返回键值对：
print(dict3.items())
#返回键：
print(dict3.keys())
#返回值：
print(dict3.values())

dict3.clear()
#endregion