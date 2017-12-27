#encoding:utf-8
import os
import shutil
#这是中午
print "HellWorld"
document = open("testfile.txt", "w+")
print "文件名: ", document.name;
document.write("这是我创建的第一个测试文件！\nwelcome!")
print document.tell()
#输出当前指针位置
document.seek(os.SEEK_SET)
#设置指针回到文件最初
context = document.read()
print context
document.close()


f = open("text.txt","w+")
paragraph = """
白日依山尽，
黄河入海流。
欲穷千里目，
更上一层楼。
"""
f.write(paragraph)

currentPath = os.getcwd()#获取当前目录路径
print  currentPath
listFileName = os.listdir(currentPath)
print "listFileName",listFileName

filePath = currentPath + "/text.txt"
if os.path.exists(filePath):
    print  "Flie text.txt is Exist"
    os.remove(filePath)
else:
    print  "Flie text.txt is not Exist"

folder = currentPath + "/tools"

if os.path.exists(folder):
    os.removedirs(folder)#只能删除空的文件夹
else:
    os.mkdir(folder)






