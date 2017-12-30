# encoding:utf-8
import urllib.request
import gzip
import re
import urllib.parse
import http.cookiejar

'''
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()


#http://blog.csdn.net/bcqtt/article/details/51584315
#https://www.cnblogs.com/xin-xin/p/4297852.html
req = urllib.request.Request('http://www.baidu.com')
response = urllib.request.urlopen(req)
the_page = response.read()
'''
def ungzip(data):
    try:
        print("尝试解压")
        data = gzip.decompress(data)
        print("解压完毕")
    except:
        print("未经压缩，不必解压")

    assert isinstance(data, data)
    return data

def getData():
    url = "http://www.baidu.com"
    data = urllib.request.urlopen(url).read()
    z_data = data.decode('UTF-8')
    print(z_data)
getData()


