import pymongo
import os

from bs4 import BeautifulSoup as bs

# Here is config
MONGO_URL = 'localhost'
MONGO_DB = 'jd'
MONGO_TABLE = 'shop'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

base_dir = "../data/rjbei/自动化抽取-京东网页集合"


class Extract_jd():

    def main(self):

        os.chdir(base_dir)
        for parent, dirnames, filenames in os.walk('.'):
            for filename in filenames:
                with open(filename, 'r') as f:
                    print(filename)
                    source = f.read()
                    self.extract(source)

    def extract(self, source):
        source = bs(source, 'lxml')
        shop_name = source.select(".jLogo")[0].text.replace("\n","")
        total_score_num = source.select(".total-score-num")[0].text.replace("\n","")
        satisfaction_product = source.select(".score-180")[0].text
        satisfaction_serve = source.select(".score-180")[1].text
        satisfaction_send = source.select(".score-180")[2].text
        satisfaction_describe = source.select(".score-180")[3].text
        satisfaction_return = source.select(".score-180")[4].text

        deal_time = source.select(".service-des-self > .value")[0].text
        dispute = source.select(".service-des-self > .value")[1].text
        repair = source.select(".service-des-self > .value")[2].text
        illegal_time = source.select(".f18.c005aa0.bold")[0].text

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

    def save_to_mongo(self, result):
        try:
            if db[MONGO_TABLE].insert(result):
                print(result)
        except Exception:
            print('存储到mongodb错误')


if __name__=="__main__":
    jd = Extract_jd()
    jd.main()