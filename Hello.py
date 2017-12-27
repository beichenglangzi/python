#-*-coding:utf-8-*-
#encoding:utf-8
import os
import sys
path = os.getcwd()
print(path)
sys.path.append(path)
import A


print("Hello world")
print("Hello,python!")  
# 司法解释

if True:
    print ("True1")
else:
  print ("False")

world = ('world')
sentence = ("this is a sentence")
paragraph = """
HEllo World !
"""
print (paragraph)
print ("Hello my world")
print ("Hello my world")

a = 10
b =  5
c = 0
print (" 1 - c 的值为：",c)
c = a + b
print (" c is ",c)

aclass = A.ClassA(2,3)
aclass.add()

