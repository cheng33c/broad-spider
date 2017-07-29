#!/bin/bash

echo "爬虫开始爬行"
cd ../cspider
scrapy crawl ebayredis --nolog
