import os

fileList = []
foldpath = os.listdir("ExtraList\\")
print(foldpath)
for f in foldpath:
    if (os.path.isfile(f)):
        fileList.append(f)
print(fileList)
