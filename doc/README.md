# 分布式爬虫系统

## 目录介绍：
	+ pic 结果截图
	+ src 提取数据，官方数据，小组结论
	+ vedio 演示视频

## 功能介绍：
	+ 爬虫系统
	+ 网页结构化

## 视频观看地址：
> 如需看简单版本演示，请看：
> <br>简明操作教程： http://v.youku.com/v_show/id_XMjg2MDEzMTY2OA==.html?spm=a2hzp.8253869.0.0
> <br>[补充简明操作教程]电商抽取：http://v.youku.com/v_show/id_XMjg4MDIxNDI2NA==.html?spm=a2h3j.8428770.3416059.1
> <br>如有不解，需看更详细演示，请看：
> 正文抽取: http://v.youku.com/v_show/id_XMjg2MDExMDI2NA==.html?f=50247773
> <br> 单机版爬虫演示: http://v.youku.com/v_show/id_XMjg2MDExMjQ0OA==.html?spm=a2h0j.8191423.item_XMjg2MDExMjQ0OA==.A&&f=50247773&from=y1.2-3.4.2
> <br> 分布式部署: http://v.youku.com/v_show/id_XMjg2MDExMjQ0OA==.html?spm=a2h0j.8191423.item_XMjg2MDExMjQ0OA==.A&&f=50247773&from=y1.2-3.4.2

### 爬虫系统
	1. 设计思路
	主从爬虫
	第一个爬虫ebayredis是用来获取链接并将获取到的链接保存到Redis中，同时可以测试链接可用性。
	第二个爬虫phdown用来下载在Redis中存放的链接。
	这么设计的原因在于爬取的速度和下载的速度不相等，所以使用双爬虫爬取。

	2. 代理池
	我们使用使用了IP代理池和ADSL拨号代理池。这么做的原因在于爬虫代理池测试结果比较不理想，速度较慢。
	IP代理池原理是爬取各大网站的免费IP地址。ADSL代理池是动态拨号生成IP地址。
	测试下来IP代理池为默认方案，ADSL拨号为备选方案。
	存储方案是将IP放到主机Redis数据库中，然后其他工作机从主机的Redis或访问网页获取代理IP进行爬行。

	3. 分布式
	我们使用了scrapyd和scrapyd-client进行分布式部署。使用Redis作为持久化数据存放。
	将爬取链接的爬虫所爬取到的链接存放在Redis中，然后下载机器从Redis中获取链接地址。
	并使用scrapyd监控爬虫爬行进度，任务执行情况。
	
	4. Redis建表策略
	    + ebayredis:start_urls 该表用于存储ebayredis爬虫爬取到的链接。
	      如果链接可用，放入phdown:tasklist中
	    + phdown:tasklist 该表用于存储要下载的链接。phdown爬虫从该表中获取链接并下载。

### 网页结构化
	1. 博客网页结构化
	使用Readability算法进行页面中正文抽取。
	正确率达到88.59%
	请看： 项目介绍/pic/博客抽取正文结果.png
	请看： 项目介绍/pic/官方数据错误抽取结果.png
	详细结果请看： 项目介绍/src/和官方数据偏差的网页(部分).txt 博客测试数据结果.txt
	从结果上看该提取正文方法取得很好的效果（抽取错误1个）。

	2. 电商网页结构化
	电商网页结构化中我们暂没有找到通法，仅找到减少人工操作的方法。
	我们使用css selector方法提取内容。人工需要将要提取的数据存入config.py中，由程序来进行抽取。最后将抽取结果保存到MongoDB中。
	详细结果请看： 项目介绍/pic/电商结构化数据提取.png
	提取了1200条左右的数据。
