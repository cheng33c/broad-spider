import pymongo
import os


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MONGO_URL = 'localhost'
MONGO_DB = 'jd'
MONGO_TABLE = 'shop'

SERVICE_AGES = ['--load-images=false', '--disk-cache=true']
browser = webdriver.PhantomJS()
# browser = webdriver.Chrome()
browser.set_window_size(1400, 900)
wait = WebDriverWait(browser,10)

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

base_dir = "/home/c/PycharmProjects/spider/cbroad/data/rjbei/自动化抽取-京东网页集合"
url_dir = "file:///home/c/PycharmProjects/spider/cbroad/data/rjbei/自动化抽取-京东网页集合"

class Extract_JD():

    def main(self):
        for parent, dirnames, filenames in os.walk(base_dir):
            for filename in filenames:
                path = os.path.join(url_dir, filename)
                self.extract_info(path)

    def extract_info(self,path):
        print(path)
        browser.get(path)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pop')))
        shop_name = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#pop > div.forBack > div:nth-child(1) > div.jHeader > div.jLogo > em"))).text
        total_score_num = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#wrap > div > div.j-rating-info > div.j-score.total-score > div > p.total-score-num > span'))).text
        satisfaction_product = wait.until(EC.presence_of_element_located(
           (By.CSS_SELECTOR, "#wrap > div > div.j-rating-info > div:nth-child(2) > div:nth-child(2) > span.score-180"))).text
        satisfaction_serve = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#wrap > div > div.j-rating-info > div:nth-child(2) > div:nth-child(3) > span.score-180"))).text
        satisfaction_send = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#wrap > div > div.j-rating-info > div:nth-child(2) > div:nth-child(4) > span.score-180"))).text
        satisfaction_describe = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#wrap > div > div.j-rating-info > div:nth-child(2) > div:nth-child(5) > span.score-180"))).text
        satisfaction_return = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#wrap > div > div.j-rating-info > div:nth-child(2) > div:nth-child(6) > span.score-180"))).text

        deal_time = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#wrap > div > div.j-rating-info > div:nth-child(3) > div.item-90 > div.service-data > div > span.service-des-self > span.value"))).text
        dispute = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#wrap > div > div.j-rating-info > div:nth-child(3) > div:nth-child(3) > div.service-data > div > span.service-des-self > span.value"))).text
        repair = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#wrap > div > div.j-rating-info > div:nth-child(3) > div:nth-child(4) > div.service-data > div > span.service-des-self > span.value"))).text
        illegal_time = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#wrap > div > div.j-rating-info > div.j-score.hegui-info > h3 > span.f18.c005aa0.bold > a"))).text

        result = {
            '店铺': shop_name,
            '店铺综合评分': total_score_num,
            '商品质量满意度': satisfaction_product,
            '服务态度满意度': satisfaction_serve,
            '物流速度满意度': satisfaction_send,
            '商品描述满意度': satisfaction_describe,
            '退换货处理满意度': satisfaction_return,
            '售后处理时长': deal_time,
            '交易纠纷率': dispute,
            '退换货返修率': repair,
            '店铺违法违规次数': illegal_time,
        }

        self.save_to_mongo(result)

    def save_to_mongo(self,result):
        try:
            if db[MONGO_TABLE].insert(result):
                print(result)
        except Exception:
            print('存储到mongodb错误')

if __name__=="__main__":
    jd = Extract_JD()
    jd.main()