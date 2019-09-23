from maoyan_spider.spiders import MaoyanSpider
from maoyan_spider.config import *
import csv
import time

if __name__ == '__main__':
    begin_time = time.time()
    d = MaoyanSpider()
    count = 0
    with open(csv_save_path, 'w', encoding='utf-8', newline='')as f:
        csv_f = csv.writer(f)
        csv_f.writerow(['filmid', 'filmname', 'boxvalue', 'releasedate'])
        for res in d.get_respones():
            for row in res:
                count += 1
                csv_f.writerow(row)
                print('****************************【已存储[ {} ]条数据，当前电影是[ {} ]，用时 [ {} ]秒】****************************'
                      .format(count, row[1], time.time() - begin_time))
