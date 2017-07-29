"""
存放爬虫通用配置信息
"""

import redis

#browser driver config
SERVICE_AGES = ['--load-images=false', '--disk-cache=true']

#mongodb config
MONGO_URI = 'localhost'

#redis config
r = redis.Redis(host='localhost',port=6379)
#redis downloader
downloader_name = "phdown:tasklist"
downloader_failed = "phdown:downloadfailed"
#redis spider
spider_name = "ebayredis:start_urls"