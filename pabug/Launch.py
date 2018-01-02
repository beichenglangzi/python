import urllib.request
import urllib.parse

def login(name,password):
    if not name :
        name = 'cl1234'
        password = '000000'

    param = {
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
    strParam = urllib.parse.urlencode(param)
    # print(strParam)
    serviceUrl = ' http://base.us.api.dbscar.com/?action=passport_service.login'
