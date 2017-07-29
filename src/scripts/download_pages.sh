#!/bin/bash

echo "开始下载爬取到的网页"
cd ../cspider
scrapy crawl phdown --nolog
