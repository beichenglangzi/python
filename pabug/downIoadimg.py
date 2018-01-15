# coding=utf-8
from icrawler.builtin import BaiduImageCrawler
from icrawler.builtin import BingImageCrawler
from icrawler.builtin import GoogleImageCrawler
"""
parser_threads：解析器线程数目，最大为cpu数目
downloader_threads：下载线程数目，最大为cpu数目
storage：存储地址，使用字典格式。key为root_dir
keyword:浏览器搜索框输入的关键词
max_num:最大下载图片数目
"""

#谷歌图片爬虫
google_storage = {'root_dir': '/Users/cl/Desktop/icrawlerLearn/google'}
google_crawler = GoogleImageCrawler(parser_threads=4,
                                   downloader_threads=4,
                                   storage=google_storage)
google_crawler.crawl(keyword='beauty',
                     max_num=10)


#必应图片爬虫
bing_storage = {'root_dir': '/Users/cl/Desktop/icrawlerLearn/bing'}
bing_crawler = BingImageCrawler(parser_threads=2,
                                downloader_threads=4,
                                storage=bing_storage)
bing_crawler.crawl(keyword='beauty',
                   max_num=10)


#百度图片爬虫
baidu_storage = {'root_dir': '/Users/cl/Desktop/icrawlerLearn/baidu'}

baidu_crawler = BaiduImageCrawler(parser_threads=2,
                                  downloader_threads=4,
                                  storage=baidu_storage)
baidu_crawler.crawl(keyword='美女',
                    max_num=10)


