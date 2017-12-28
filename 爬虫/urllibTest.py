# encoding:utf-8
import urllib.request
response = urllib.request.urlopen('')
html = response.read()
print(html)

