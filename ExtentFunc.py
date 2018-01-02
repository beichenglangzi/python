# 功能已经定下来了
# 有没有一种方法给它动态的增加功能
def plus(func):
    #先拿到func
    the_list = [0]
    def plus_func(*args, **kwargs):
        func(*args,**kwargs)
        the_list[0] +=1
    return plus_func
def func():
    print("Hello Test")
funcTest = plus(func())

def testPrint():
    print("testPrint")

funcTestPrint = plus(testPrint())