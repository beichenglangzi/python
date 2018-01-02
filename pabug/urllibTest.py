# encoding:utf-8
import urllib.request
import urllib

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
# print(data)

#http://blog.csdn.net/bcqtt/article/details/51584315
#https://www.cnblogs.com/xin-xin/p/4297852.html


data = {}
data['word'] = 'Jecvay Notes'

url_values = urllib.parse.urlencode(data)
#data是一个字典, 然后通过urllib.parse.urlencode()来将data转换为 ‘word=Jecvay+Notes’的字符串,
# 最后和url合并为full_ur
url = "http://www.baidu.com/s?"
full_url = url + url_values

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)


