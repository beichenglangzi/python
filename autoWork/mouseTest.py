#-*-coding:utf-8-*-
import pyautogui,time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
pyautogui.size()
# for i in  range(10):
#     pyautogui.moveTo(100,100,duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
    # pyautogui.moveTo(200, 200, duration=0.25)
    # pyautogui.moveTo(100, 200, duration=0.25)
    # pyautogui.moveTo(300, 100, duration=0.25)
    # pyautogui.moveTo(100, 400, duration=0.25)
    # pyautogui.moveTo(500, 100, duration=0.25)
    # pyautogui.moveTo(100, 600, duration=0.25)

# for i in range(1):
#     pyautogui.moveRel(100, 0, duration=0.25)
#     pyautogui.moveRel(0, 100, duration=0.25)
#     pyautogui.moveRel(-100, 0, duration=0.25)
#     pyautogui.moveRel(0, -100, duration=0.25)

# try:
#     while True: #TODO: GEt And Print The mouse cordinates
#         pyautogui.moveRel(100, 0, duration=0.25)
#         pyautogui.moveRel(0, 100, duration=0.25)
#         pyautogui.moveRel(-100, 0, duration=0.25)
#         pyautogui.moveRel(0, -100, duration=0.25)
# except KeyboardInterrupt:
#     print('\nDone')
print("开始程序")
# for i in range(5):
#     time.sleep(1)
#     print("还剩下:",(5-i),"秒")
# pyautogui.position() #获取当前鼠标位置
# x, y = pyautogui.position()
# positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
# print(positionStr, end='')
# print("World")

# pyautogui.click() # click to put drawing program in focus
# distance = 200
# a = 1
# while distance > 0:
#     pyautogui.dragRel(distance, 0, duration=0.1) # move right
#     distance = distance - 3
#     pyautogui.dragRel(0, distance, duration=0.1) # move don
#     pyautogui.dragRel(-distance, 0, duration=0.1) # move left
#     distance = distance - 3
#     pyautogui.dragRel(0, -distance, duration=0.1) # move up


# print("end Print")
# pyautogui.scroll(100)
# im = pyautogui.screenshot()
# im.save("Screenshot.png")#截屏
# im.getpixel((50,200))
# pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))#给定坐标处的颜色应该“完全”匹配。即使只是稍有差异(例如，是(255， 255，254)而不是(255，255，255))，那么函数也会返回 False。

# positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
# pixelColor = pyautogui.screenshot().getpixel((x, y))
# positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
# positionStr += ', ' + str(pixelColor[1]).rjust(3)
# positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
# print(positionStr, end='')
#
# list = list(pyautogui.locateOnScreen("QQ.png"))
# if len(list) > 0:
#     print("找到这个图标")
#     qqFram = list[0] #因为QQ我的电脑中只安装了一个，所以就只有一个QQ的坐标
#     print(qqFram)
#     qqCenter = pyautogui.center(qqFram)#获取QQ的中心坐标
#     pyautogui.click(qqCenter)


pyautogui.click(100,100)
pyautogui.typewrite("Hello World",interval=0.25)
pyautogui.keyDown("shift")
pyautogui.press("4")
pyautogui.keyUp("shift")