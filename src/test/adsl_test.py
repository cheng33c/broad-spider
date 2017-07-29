"""
该程序是自动化测试当前ADSL-Proxy的可用性
"""


import redis
import time

from urllib import response
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from adslproxy import RedisClient, server

client = redis.Redis(host='120.24.231.4', password="redistest")

# browser driver
SERVICE_AGES = ['--load-images=false', '--disk-cache=true']
browser = webdriver.PhantomJS(service_args=SERVICE_AGES)
browser.set_window_size(1400, 900)

client = RedisClient(host='120.24.231.4', password='redistest', port='6379')

link = "http://www.github.com"

class Test_Adsl():

    def adsl_test(self,mylink):
        try:
            ip = client.random()
            print('use ip:' + ip)
            SERVICE_AGES.append('--proxy=' + ip)
            browser.get(mylink)
            time.sleep(0.2)
            doc = browser.page_source
            print(doc)
            for href in hrefs:
                self.adsl_test(href)

        except TimeoutException:
            return self.parse(response)


if __name__=="__main__":
    myadsl = Test_Adsl()
    myadsl.adsl_test(link)