import PIL
from PIL import Image
import os
import xlwt
class Ptrancefrom(object):

    def __init__(self,img,width,heigth):
        self.img = img
        self.width = width
        self.heigth = heigth
        self.ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    def get_char(self,r,b,g,a):

        if a == 0:
            return ''
        length = len(self.ascii_char)

        gray = int(0.2126 *r + 0.7152*g + 0.0722*b)
        unit = (256.0 + 1) / length
        return self.ascii_char[int(gray / unit)]

    def print_picture(self):
        #'打印图形'
        # 打开图片
        im = Image.open(self.img)
        # 设置图片像素的大小
        im = im.resize((self.width, self.heigth), Image.NEAREST)

        txt = ""

        for i in range(self.heigth):
            for j in range(self.width):
                (r,g,b,a) = im.getpixel((j,i))
                txt += self.get_char(r,g,b,a)

            txt += '\n'

        print(txt)
        document = open("acii_Pic.txt", "w+")
        document.write(txt)

img = Image.open("dogtest.png")
assert isinstance(img,Image.Image)
(imW,imH) = img.size
pic = Ptrancefrom("he.png",imW,imH)#drawing
pic.print_picture()