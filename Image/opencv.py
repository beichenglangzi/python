# coding=utf-8
import site
site.addsitedir("/Users/cl/Documents/python/venv/lib/python3.6/site-packages/")
import wx
# import virtualenv
import sys
app = wx.App()
window = wx.Frame(None, title = "wxPython - www.yiibai.com", size=(400,300))
panel = wx.Panel(window)
label = wx.StaticText(panel, label = "Hello World", pos=(100,100))
window.Show(True)
app.MainLoop()
