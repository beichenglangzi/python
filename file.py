#encoding:utf-8
import os
import shutil
from Pythonclass import CopyFileExcute

#这是中午
print ("HellWorld")
document = open("testfile.txt", "w+")
print ("文件名: ", document.name)
document.write("这是我创建的第一个测试文件！\nwelcome!")
print (document.tell())
#输出当前指针位置
document.seek(os.SEEK_SET)
#设置指针回到文件最初
context = document.read()
print (context)
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
print(currentPath)

listFileName = os.listdir(currentPath)
print ("listFileName",listFileName)

filePath = currentPath + "/text.txt"
if os.path.exists(filePath):
    print  ("Flie text.txt is Exist")
    os.remove(filePath)
else:
    print  ("Flie text.txt is not Exist")

folder1 = currentPath + "/tools"

if not os.path.exists(folder1):
    #os.removedirs(folder1)#只能删除空的文件夹
    os.mkdir(folder1)




folder2 = currentPath + "/tool"

if not os.path.exists(folder2):
   os.mkdir(folder2)

toolFileName = folder2 + "/text.txt"
f = open(toolFileName,"w+")
f.write(paragraph)
f.flush()
f.seek(0)
print(f.read())
print("toolFileName")
f.close()
print(toolFileName)

#os.chdir(folder1)
print("当前路径"+os.getcwd())

toolsFilePath = folder1+"/text.txt"
if not os.path.exists(toolsFilePath):
    fp = open(toolsFilePath,"w+")
    fp.close()
print(toolsFilePath)
'''
#copy 文件从tool 到 tools

shutil.copyfile(folder1,toolFileName)
print(os.listdir(folder1))
f = open("text.txt")
f.seek(0)
print(f.read())
f.close()
'''
print("-----")
print(toolFileName)
print(toolsFilePath)
print("-----")
CopyFileExcute.copyFile(toolFileName,toolsFilePath)


