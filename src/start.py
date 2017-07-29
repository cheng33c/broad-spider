import os

def start_crawl_links():
    pass

def start_download_pages():
    pass

def start_extract_blog():
    pass

def start_extract_ebay():
    pass

def manage_spider():
    pass

def main():
    print('欢迎使用分布式爬虫系统v0.1\n'
          '1.爬取链接地址\n'
          '2.下载网页\n'
          '3.提取博客内容\n'
          '4.提取电商内容\n'
          '5.管理爬虫\n'
          '请输入你的选择:')
    choice = input(int)
    if (choice == 1): start_crawl_links()
    elif (choice == 2): start_download_pages()
    elif (choice == 3): start_extract_blog()
    elif (choice == 4): start_extract_ebay()
    elif (choice == 5): manage_spider()

if __name__=='__main__':
    os.chdir('scripts')
    main()