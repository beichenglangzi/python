# encoding:utf-8
import urllib.request
import urllib.parse
import json
import sys
import os
path = os.getcwd()
print(path)
sys.path.append(path)
import Manager

def login(name='cl1234',password='111111'):
    pargram = {
        'login_key':name,
        'password': password,
        'app_id': '8311',
        'lan': 'zh',
        'time': '1514874719.93839',
        'd_model': 'iPod Touch 5',
        'imei': '',
        'config_area': '1',
        'config_no': '94'
        }
    strParam = urllib.parse.urlencode(pargram)
    strParam = strParam.encode('utf-8')
    serviceUrl = ' http://base.us.api.dbscar.com/?action=passport_service.login'
    request = urllib.request.Request(serviceUrl)
    f = urllib.request.urlopen(request,strParam)
    # print(strParam)
    # print(f.read().decode('utf-8'))
    return f.read().decode('utf-8')


logDic = json.loads(login())
print(logDic)
data = logDic['data']
print(logDic)
print(logDic['code'])
print(logDic['data'])

u = Manager.User()
u.token = data['token']
u.token1 = data['token']
u.user_id = data['user']['user_id']
u.user_name = data['user']['user_name']
u.nick_name = data['user']['nick_name']
u.email = data['user']['email']
print(u.token1)


