#-*-coding:utf-8-* print("end Print")
from icrawler.builtin import BaiduImageCrawler
from pathlib import Path
#指定图片存放位置
imagePath = "/Users/chenjinlong/Desktop/downloadImage"
f = Path(imagePath)
#指定要搜索的关键字列表
keywords = ["速度与激情8","再见前任","芳华","西游记女儿国","大世界","妖猫传"]
for keyword in keywords:
    #创建以关键字命名的文件夹
    destFolder = f.joinpath(keyword)
    try:
        f.mkdir(777,keyword)
    except FileExistsError:
        print("file existed already!")
    #调用模块下载图片
    baidu_crawler = BaiduImageCrawler(storage={"root_dir":str(destFolder)})
    baidu_crawler.crawl(keyword=keyword,offset=0,max_num=10,min_size=0,max_size=0)