"""
    使用phantomjs模拟访问下载。
"""

# -*- coding: utf-8 -*-
import time
import os
import re

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from scrapy_redis.spiders import RedisSpider
from readability.readability import Document
from .general_config import *
from .downloader_config import *


# browser driver
browser = webdriver.PhantomJS(service_args=SERVICE_AGES)
browser.set_window_size(1400, 900)

class PhdownSpider(RedisSpider):
    name = "phdown"
    redis_key = downloader_name
    download_count = 0

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(PhdownSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        """ 抽取页面中所有可用的链接 """
        r.lpop(downloader_name)
        link = response.url
        try:
            browser.get(link)
            time.sleep(0.2)
            self.download_count += 1
            print('[' + str(self.download_count) + '] Downloading : ' + link)
            self.download_url_min(self.build_path1(link))
        except TimeoutException:
            r.rpush(downloader_failed,r.lpop(downloader_name))
            print(link + "无法访问")
            return self.parse(response)

    def download_url_min(self,path):
        """
        该方法只下载网页中的Html代码，不下载js css代码
        :param dir: 保存文件目录
        :param url: 要下载的网址
        :return:
        """
        print(path)
        html = Document(browser.page_source).content()
        with open(path, 'w') as f:
            f.write(html)

    def build_path1(self, url):
        url = url.split("/")
        path = ""
        for v in url: path += v
        if (os.path.exists(save_dir) == False): os.makedirs(save_dir)
        path = save_dir + path
        return path

    def build_path2(self,url):
        """
        该方法主要用于构建Html文件保存路径
        如果你需要分门别类的保存网站数据，请使用该函数
        它的工作包括检测文件目录是否存在，创建文件目录，构建文件名
        :param url: 网页网址
        :return:
        """
        # 用匹配网站名(e.g. http://www.taobao.com 结果: taobao)创建文件夹
        pattern1 = re.compile('https?://(.*?)/?$')
        website_name = pattern1.match(url).group(1).split('.')[1]
        file_path = save_dir + website_name + '/'
        # 判断是否有该网站的文件夹，如果没有，则创建该文件夹
        if (os.path.exists(file_path) == False): os.makedirs(file_path)
        # 匹配文件名，我们取URL最后一个'/'后面的字符作为文件名
        file_path = file_path + url.split('/')[-1]
        return file_path