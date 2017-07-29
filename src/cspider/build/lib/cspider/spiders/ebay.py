# -*- coding: utf-8 -*-
import scrapy
import pymongo
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from scrapy_redis.spiders import RedisCrawlSpider
from pybloom import BloomFilter
from .general_config import *

#browser driver
browser = webdriver.PhantomJS(service_args=SERVICE_AGES)
wait = WebDriverWait(browser,10)
browser.set_window_size(1400,900)

client = pymongo.MongoClient()
db = client['ebay']
links = BloomFilter(capacity=10000, error_rate=0.001)

class EbaySpider(scrapy.Spider):
    name = "ebay"
    allowed_domains = ["www.taobao.com"]
    start_urls = ['https://www.taobao.com']

    def parse(self, response):
        """ 抽取页面中所有可用的链接 """
        try:
            browser.get(response.url)
            time.sleep(0.5)
            hrefs = response.xpath('//a/@href').extract()

            for href in hrefs:
                if (pattern1.match(href)): continue
                if (pattern2.match(href)): href = pattern2.sub('',href)
                if (links.add(href) == True): continue
                print(href)
                r.rpush("ebay_start_urls",href)

        except TimeoutException:
            return self.parse(response)

        finally:
            browser.close()
