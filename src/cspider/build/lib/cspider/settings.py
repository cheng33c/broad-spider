# -*- coding: utf-8 -*-

# Scrapy settings for cspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'cspider'

SPIDER_MODULES = ['cspider.spiders']
NEWSPIDER_MODULE = 'cspider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'cspider.middlewares.CspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'cspider.middlewares.CustomDownloaderMiddleware': 543,
#}
#DOWNLOADER_MIDDLEWARES = {
#    'cspider.pipelines.rotate_useragent.RotateUserAgentMiddleware' :400
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
EXTENSIONS = {
    #'scrapy.extensions.telnet.TelnetConsole': None,
    #'scrapy.extensions.logstats.LogStats': 300,
    #'scrapy.extensions.corestats.CoreStats': 400,
    #'scrapy.extensions.memusage.MemoryUsage': 500,
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'cspider.pipelines.CspiderPipeline': 300,
#    'scrapy_redis.pipelines.RedisPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# my config
LOG_LEVEL = 'DEBUG'

#BloomFilter On Redis config
FILTER_URL = None
FILTER_HOST = 'localhost'
FILTER_PORT = 6379
FILTER_DB = 0
# REDIS_QUEUE_NAME = 'OneName'   # 如果不设置或者设置为None，则使用默认的，每个spider使用不同的去重队列和种子队列。如果设置了，则不同spider共用去重队列和种子队列

"""
    这是去重队列的Redis信息。
    原先的REDIS_HOST、REDIS_PORT只负责种子队列；由此种子队列和去重队列可以分布在不同的机器上。
"""

# Enable Scrapy-Redis
#scrapy-redis config

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# Specify the host and port to use when connecting to Redis (optional).
#REDIS_HOST = 'localhost'
#REDIS_PORT = 6379
#REDIS_URL = 'redis://root:redistest@120.24.231.4:6379'

# bloomfilter-on-redis config
# Enables scheduling storing requests queue in redis.
#SCHEDULER = 'cspider.scrapy_redis.scheduler.Scheduler'
#SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = 'cspider.scrapy_redis.queue.SpiderPriorityQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapyWithBloomfilter_demo.scrapy_redis.queue.SpiderSimpleQueue'
# Ensure all spiders share same duplicates filter through redis.
#DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# Specify the host and port to use when connecting to Redis (optional).
#REDIS_HOST = 'localhost'
#REDIS_PORT = 6379