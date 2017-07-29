# 分布式爬虫系统
## 队名： Morris
## 队员： 陈诚 韩存鑫 周立禅
## 指导老师： 张立凡

## 安装方法
> Debian/Ubuntu/Mint: 
> <br>sudo apt install python3 python3-pip
> <br>sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
> <br> pip3 -r install requirements.txt

## 使用方法（评委）

## 方法1：
### 连接主机
ssh root@112.74.77.166
<br>Chen0814t
<br>cd Broad-Spider-src/scripts
### 运行爬虫
连接爬虫运行： sh run-spider.sh
<br>下载爬虫运行： sh download_pages.sh
### 运行分布式部署
ssh root@120.24.231.4
<br>cd usr
<br>Chen0814tt
<br>（注：切换回112.74.77.166主机）
<br>sh deploy.sh
<br>sh scheduler-ebay.sh
<br>sh scheduler-download.sh

### 运行网页结构化
sh extract-blog.sh

## 方法2：

ssh root@112.74.77.166
<br>cd Broad-Spider-src/scripts
<br>ssh root@120.24.231.4
<br>cd usr
<br>(切换回112.74.77.166)
<br>（注： start-now.sh是上面脚本集合执行，可能需要等待比较长的时间）
<br>sh start-now.sh


## 使用方法视频介绍
请看： 项目介绍/使用方法.mp4

## 目录结构
	+ cmlnl 网页结构化程序
	+ cspider 网页爬虫程序
		+ phdown 爬虫下载程序
		+ ebayredis 网址获取程序
	+ csite Django 前端管理程序 （待完善）
	+ data 官方数据集
	+ test 测试程序
	+ tools 工具集
	+ scripts 快速执行脚本
	+ requirements.txt 程序所需依赖
	+ README.md 介绍文档
	+ ghostdriver.log selenium驱动程序日志
