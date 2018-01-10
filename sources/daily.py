# coding=utf-8

def forecast():
    '模拟每天天气预报'
    return  '和昨天一样'


if __name__ == '__main__':
    print("Content-type:text/html")
    print()  # 空行，告诉服务器结束头部
    print('<html>')
    print('<head>')
    print('<meta charset="utf-8">')
    print('<title>Hello Word - 我的第一个 CGI 程序！</title>')
    print('</head>')
    print('<body>')
    print('<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>')
    print('</body>')
    print('</html>')
