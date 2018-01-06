from PIL import ImageColor
from PIL import Image,ImageDraw,ImageFont
import os
b = ImageColor.getcolor('Red','RGBA')
# print(b)

img = Image.open('dogtest.png')
assert isinstance(img,Image.Image)
cutImage = img.crop((43,29,79,63))
cutImage.save("cutImage.png")

#测试拷贝图片
copyImage = img.copy()
copyImage.paste(cutImage,(0,0))
copyImage.paste(cutImage,(0,100-34))
copyImage.save("copyImage.png")

#测试旋转
rotateImage = img.copy()
rotateImage.rotate(90).save("roteImage.png")

#改变单个像素   getpixel()和 putpixel()方法取得和设置
im = Image.new('RGBA',(100,100))     #获取一个 100X100的透明图像
for x in range(100):
    for y in range(50):
        im.putpixel((x,y),ImageColor.getcolor('darkgray','RGBA'))        #在上半部分填充颜色
im.save("createImage.png")
imgMap = img.copy()
mapImage = imgMap.resize((50,15),Image.ANTIALIAS)
#把imgMap贴在创建图片的右下角
(imW,imH) = im.size
(imgMapW,imgMapH) = mapImage.size
im.paste(mapImage,(imW - imgMapW,imH - imgMapH))
im.save("mapImage.png")

im = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(im)
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')   #正方形
draw.ellipse((120, 30, 160, 60), fill='red')          
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),
fill='brown')
for i in range(100, 200, 5):
    draw.line([(i, 0), (200, i - 100)], fill='green')

draw.text((20, 150), 'Hello', fill='purple')
draw.text((100, 150), 'Howdy', fill='gray')
im.save("drawing.png")
# http://blog.csdn.net/xiaodangshan/article/details/64540157