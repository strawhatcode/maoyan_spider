import datetime
import time

import pandas as pd
import csv
begin_time = time.time()

def filter1():
    df = pd.read_csv('film_rank.csv')
    #把date列的值转成datetime类型
    df['date'] = pd.to_datetime(df['date'])
    #排序
    sort_data = df.sort_values(['name', 'date'], ascending=[True, True])
    #重置索引
    reset_data = sort_data.reset_index(drop=True)

    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.width', None)
    #
    end_date = datetime.datetime.strptime('2019-09-22', '%Y-%m-%d')
    count = 0
    print("-------------【已加载数据，用时[ {} ]】-------------".format(time.time() - begin_time))
    with open('aaaaaaa.csv', 'w', encoding='utf-8', newline='') as f:
        csv_f = csv.writer(f)
        csv_f.writerow(['filmid', 'name', 'releasedate', 'date', 'value'])
        last_date = ''  #记录上一行的日期
        last_id = ''    #记录上一行的id
        last_list = []  #记录上一行的信息

        for i in range(len(reset_data)):
            #如果第一行就继续循环
            if i == 0:
                continue
            #临时存放数据的列表
            temp_list = [reset_data.at[i, 'filmid'], reset_data.at[i, 'name'], reset_data.at[i, 'releasedate'],
                         reset_data.at[i, 'date'], reset_data.at[i, 'value']]
            cur_date = temp_list[3]   #当前的日期
            #如果循环到第二行直接把信息存储起来
            if i == 1:
                count += 1
                csv_f.writerow(temp_list)
                last_date = temp_list[3]
                last_id = temp_list[0]
                last_list = temp_list
                print("***********************【已解析[ {} ]条数据，用时[ {} ],数据[ {} ]】***********************"
                      .format(count, time.time() - begin_time, temp_list))
                continue
            #判断当前行与上一行的id是否相同
            if temp_list[0] == last_id:
                #两行的天数差
                date_minus = (cur_date - last_date).days
                #如果只相差一天则直接存储数据
                if date_minus == 1:
                    count += 1
                    csv_f.writerow(temp_list)
                    # last_date = cur_date
                    print("***********************【已解析[ {} ]条数据，用时[ {} ],数据[ {} ]】***********************"
                          .format(count, time.time() - begin_time, temp_list))
                #如果相差多天则把空着的天补上
                else:
                    for j in range(date_minus):
                        count += 1
                        #如果相差天数的最后一天，则把当前行的天数赋给临时列表
                        if j == date_minus - 1:
                            temp_list[3] = cur_date
                        else:
                            temp_list[3] = last_date + datetime.timedelta(days=1)
                        print("***********************【已解析[ {} ]条数据，用时[ {} ],数据[ {} ]】***********************"
                              .format(count, time.time() - begin_time, temp_list))
                        csv_f.writerow(temp_list)
                        last_date = temp_list[3]
                last_date = temp_list[3]
                last_id = temp_list[0]
                last_list = temp_list
            #如果当前行的id与上一行的id不相同
            else:
                date_minus2 = (end_date - last_date).days
                #判断上一行的数据日期，如果比最终天数少，则把天数按最终数据补上
                for ii in range(date_minus2):
                    last_list[3] = last_date + datetime.timedelta(days=1)
                    csv_f.writerow(last_list)
                    last_date = last_list[3]
                    print("***********************【已解析[ {} ]条数据，用时[ {} ],数据[ {} ]】***********************"
                          .format(count, time.time() - begin_time, temp_list))
                csv_f.writerow(temp_list)
                last_date = cur_date
                last_id = temp_list[0]
                print("***********************【已解析[ {} ]条数据，用时[ {} ],数据[ {} ]】***********************"
                      .format(count, time.time() - begin_time, temp_list))

filter1()




