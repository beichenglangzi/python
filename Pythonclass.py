class CopyFileExcute:
    def __init__(self):
        print("构造函数")
    def __del__(self):
        print("析构函数")
    def copyFile(self,srcPath, destPath):
        print("""helllo""")
        print(srcPath)
        print(destPath)
        f1 = open(srcPath,"r")
        f2 = open(destPath,"a")

        for line in  f1.readlines():
            f2.write(line)
        f2.flush()
        f2.seek(0)
        print(f2.read())

        f1.close()
        f2.close()


del CopyFileExcute
 '''
class CopyFileExcute:
    def __init__(self):#前后都是两个下划线
        print("构造函数")
    def __del__(self):#前后都是两个下划线
        print("析构函数")

    def copyFile(self, srcPath, destPath):
        f1 = open(srcPath, "r")
        f2 = open(destPath, "a")

        for line in f1:
            f2.write(line)

        f1.close()
        f2.close()

#copyFileExcute = CopyFileExcute()
#copyFileExcute.copyFile("text1.txt", "text2.txt")
del copyFileExcute
 '''