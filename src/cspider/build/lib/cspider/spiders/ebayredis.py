# -*- coding: utf-8 -*-

import time
import requests

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from cspider.scrapy_redis.spiders import RedisSpider
from pybloom import BloomFilter
from adslproxy import RedisClient, server
from .general_config import *
from .spider_config import *

browser = webdriver.PhantomJS(service_args=SERVICE_AGES)
browser.set_window_size(1400, 900)

bloom_links = BloomFilter(capacity=100000, error_rate=0.001)
client = RedisClient(host='120.24.231.4', password='redistest', port='6379')

PROXY_POOL_URL = 'http://localhost:5000/get'

class EbayredisSpider(RedisSpider):
    name = "ebayredis"
    redis_key = spider_name
    index_count = 0
    baseurl = ''
    ip = ""

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        #r.rpush(spider_name, "http://www.taobao.com")
        self.allowed_domains = filter(None, domain.split(','))
        super(EbayredisSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        """ 抽取页面中所有可用的链接 """
        r.lpop(spider_name)
        link = response.url
        try:
            # browser driver
            browser.get(link)
        except TimeoutException:
            if self.ip != None:
               proxy = '--proxy=' + self.ip
               SERVICE_AGES.append(proxy)
            return self.parse(response)

        time.sleep(0.2)
        r.rpush(downloader_name, link)
        hrefs = response.xpath('//a/@href').extract()

        for href in hrefs:
            # 是否符合规则，符合规则按规则处理url
            if (pattern1.match(href) or pattern4.match(href) or
                            href=='' or href[0]=='#' or bloom_links.add(href) == True): continue
            if (pattern2.match(href)): href = pattern2.sub('',href)
            if (pattern3.match(href) == None): href = 'http://' + href
            if (pattern5.match(href)): continue
            self.index_count += 1
            print('[' + str(self.index_count) + '] Indexing : ' + href)
            r.rpush(spider_name,href)


    def get_proxy(self):
        """
        该方法从 IP代理池 获取IP
        :return:
        """
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                return response.text
        except ConnectionError:
            return None