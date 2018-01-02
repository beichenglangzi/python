# encoding:utf-8
import urllib.request
import urllib.parse
import json

def login(name='cl1234',password='000000'):
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
    return  f.read().decode('utf-8')


logDic = json.loads(login())
print(logDic)
print(logDic['code'])
print(logDic['data'])