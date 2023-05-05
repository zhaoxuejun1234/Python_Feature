import os
os.makedirs("file",exist_ok=True)
# with open("file/text.txt","a+") as f:
#     f.write("abc")
# f.close()
with open("file/text.txt","r+") as f:
    print(f.read())
f.close()