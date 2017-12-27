
class CopyFileExcute:
    def __init__(self):
        print("构造函数")
    def __del__(self):
        print("析构函数")
    def copyFile(srcpath: object, destpath: object) -> object:
        print("""helllo""")
        print(srcpath)
        print(destpath)
        f1 = open(srcpath,"r")
        f2 = open(destpath,"a")

        for line in  f1.readlines():
            f2.write(line)
        f2.flush()
        f2.seek(0)
        #f2 = open(destpath)
        #r = f2.read()
        #print(r)

        f1.close()
        f2.close()
    def cprint(self):
         print("Hello Class CopyFileExcete")



