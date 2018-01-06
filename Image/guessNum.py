import sys
import types
import random
a = sys.argv[0] #sys.argv[0]表示代码本身文件路径
print(a)
# a = sys.argv[1] 1 运行的时候需要输入其他的参数，作为运行的一部分

secret = random.randrange(1,30)
# secret = random.randrange(1000)
print(secret)


gg = 1
while gg == 1:
    a = input("猜猜这个数字：")
    if not a.isdigit():
        print("对不起，输入不合法，请输入数字")
        continue
    guess = int(a)
    print(guess)

    if guess < secret:
        print("sorry,猜小了")
    elif guess > secret:
        print("sorry，猜大了")
    else:
        print("恭喜你才对了")
        gg = 0

x = input("请输入数组，用空格分开")
x = x.split(' ')
print(type(x))
tup = []
for c in x:
    if not c == '':
        if c.isdigit():
            if int(c):
                print(c)
                tup.append(int(c))
        else:
            print(c,"为无效数字，输入不合法")

print(tup)

