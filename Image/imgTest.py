from PIL import ImageColor
from PIL import Image
import colorsys
import os

# col = ImageColor.getcolor('red','RGBA')
# print(col)
# dogIm = Image.open('dog.png')
# assert isinstance(dogIm, Image.Image)
# (width, hight) = dogIm.size
# print(dogIm.size,width,hight,dogIm.filename,dogIm.format_description)
# newPng = dogIm.resize((100,100),Image.ANTIALIAS)
# newPng.save("newPng.png")
# dogIm.save('dog1.png')
# print(newPng.size)
def imageBatch():
    currentPath = os.getcwd()
    resultImgPath = currentPath + "/resultImage"
    resouceImagePath = currentPath + "/resouceImage"
    if os.path.exists(resouceImagePath) & os.path.exists(resultImgPath):
        print("初始化路径完成")
    imgList = os.listdir(resouceImagePath)
    imgNameList = []
    imgcount = len(imgList)
    cuttentProgess = 0
    if imgcount > 0:
        for imgname in imgList:
            cuttentProgess += 1
            os.chdir(resouceImagePath)
            if not imgname.endswith(".png"):
                continue
            img = Image.open(imgname)
            assert isinstance(img, Image.Image)
            (w, h) = img.size
            imgname = imgname.split(".png")[0]
            imgPath = resultImgPath + "/" + imgname
            if not os.path.exists(imgPath):
                os.mkdir(imgPath)
            os.chdir(imgPath)
            for i in range(1, 4):
                newPng = img.resize((int(w * i / 3), int(h * i / 3)), Image.ANTIALIAS)
                if i == 1:
                    newPngName = imgname + ".png"
                elif i == 2:
                    newPngName = imgname + "@2x.png"
                else:
                    newPngName = imgname + "@3x.png"
                newPng.save(newPngName)
            print("当前进度为:%.2f" % (cuttentProgess * 100 / imgcount), "%")

    else:
        print("要处理的文件夹为空，请放入要处理的图片")

# imageBatch()



def getAllColorsFromImage():
    colorArr = []
    imW = 0
    imH = 0
    imgPath = "dog.png"
    path = os.getcwd()
    father_path = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
    grader_father = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")
    imgPath = father_path + "/Image" + "/dog.png"
    if not imgPath:
        imgPath = "dog.png"

    if os.path.exists(imgPath):
        im = Image.open(imgPath)
        assert isinstance(im,Image.Image)
        im = im.convert("RGBA")
        (imW, imH) = im.size
        maxEdage = 200
        if (imW > maxEdage or imH > maxEdage):
            temp = max(imH,imW)
            imW = int(imW*maxEdage/temp)
            imH = int(imH*maxEdage/temp)
            im.thumbnail((imW,imH))
            im.save("thumbnail.png")

        for i in range(imW):
            for j in range(imH):
                # print("ij",i,j)
                # print(im.getpixel((i,j)))
                # (r, g, b, a) = im.getpixel((j, i))
                # # print(r,g,b,a)
                # # print(im.getpixel((j, i)))
                # print(type(im.getpixel((i,j))))
                colorArr.append(im.getpixel((i,j)))

    else:
        print("path is error")

    return (colorArr, imW, imH)
# print(getAllColorsFromImage())

