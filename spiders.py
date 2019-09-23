
import requests
import json
import time
import datetime
import random
from maoyan_spider.config import *


class MaoyanSpider:
    #请求头，随机使用一个UA
    def headers(self):
        header = {
            'user-agent': random.choice(UserAgent)
        }
        return header

    #解析参数，把参数保存成一个列表
    def parse_params(self):
        date_list = []
        begin = datetime.datetime.strptime(beginDate, '%Y%m%d')
        end = datetime.datetime.strptime(endDate, '%Y%m%d')
        while True:
            if begin <= end:
                date = ''
                temp_date_list = str(begin)[0:10].split('-')
                for temp_date in temp_date_list:
                    date += temp_date
                date_list.append(date)
                begin = begin + datetime.timedelta(days=1)
            else:
                break
        return date_list

    #发送请求
    def get_respones(self):
        url = 'http://piaofang.maoyan.com/second-box?beginDate='
        params_list = self.parse_params()
        for param in params_list:
            time.sleep(random.random()+0.2)  #休眠0.2~1.2秒再发送请求
            res = requests.get(url=url + param, headers=self.headers())
            yield self.parse_data(res.text, param)
            # print(res.text)

    #分析数据
    def parse_data(self, res, date):
        data_list = []
        datas = json.loads(res)
        for data in datas['data']['list']:
            _date = datetime.datetime.strptime(date, '%Y%m%d')
            temp_list = [data['movieId'], data['movieName'], data['boxInfo'], data['releaseInfo'], str(_date)[0:10]]
            data_list.append(temp_list)
        return data_list





