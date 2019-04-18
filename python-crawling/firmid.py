# -*- coding: utf-8 -*-
import requests
import re
import time
import random
import math
import os
from lxml import etree
import xlrd
import xlwt
from selenium import webdriver
data = xlrd.open_workbook("vc_data.xls")
table = data.sheets()[0]  # 0表示excel第一张sheet表
firm_id = table.col_values(0)  # 获取excel第一列中的所有值并保存为列表
firm_name = table.col_values(2)
firm_address = table.col_values(1)

agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0)'
url = 'https://www.qichacha.com/search?key='
url2 = 'https://www.qichacha.com/firm_6a32ccc355c8e66df4f420e09a2bd06b.shtml'
headers = {
        "User-Agent": agent,
        'Cookie':'acw_tc=73e72d9515531600538066439e8652d01172ca8f303c7c4bb99867dbb6; QCCSESSID=6oqrbos8c1ib06qhjv0r6qt1t1; zg_did=%7B%22did%22%3A%20%221699f8da8a5f-0ea2421217fc5d-12666d4a-13c680-1699f8da8a61c4%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201553160054954%2C%22updated%22%3A%201553160158940%2C%22info%22%3A%201553160054959%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%222ccae7422e17e3bd5f508b3315848432%22%7D; UM_distinctid=1699f8daeb09b7-0968ee97c127e28-12666d4a-13c680-1699f8daeb1fc; CNZZDATA1254842228=181018681-1553159263-%7C1553159263; _uab_collina=155316005744353231354253; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1553160058; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1553160160'
            }

def crawl_firm_code(key_1,key_2):

    try:

        result = requests.get(key_1,headers=headers,timeout = 10).text
        time.sleep(5)
        #result = chrome.get(key_1).text
        #print(result)
        if '小查还没找到数据' in result:
            result = requests.get(key_2,headers=headers,timeout = 10).text
            time.sleep(5)
            if '小查还没找到数据' in result:
                firm_code = '-'
            else:
                pattern = r'href="/firm_(.*?).html'
                firm_code = re.findall(pattern, result, re.S)[0]
            #result = chrome.get(key_2).text
           # print(result)
        else:
            pattern = r'href="/firm_(.*?).html'
            firm_code = re.findall(pattern, result, re.S)[0]

        return firm_code
    except Exception as e:
        print(e)
        #firm_code = '出错了'


#detect_url = 'http://httpbin.org/ip'
#proxies = crawlproxy()
def mainfunc():
    file = xlwt.Workbook()
    table = file.add_sheet('sheet1')
    for i in range(1,len(firm_id)):

        key_1  = url+firm_name[i] +'+'+ firm_address[i]
        key_2 = url + firm_name[i]
        #try:
        firm_key = crawl_firm_code(key_1, key_2)
        # except Exception as e:
        #     firm_code = '无'
        print(firm_key)
        #f.write(str(firm_id[i])+']'+firm_name[i]+']'+firm_address[i]+']'+firm_key)
        #VC_id	VC_address	公司名	搜到的公司名	股东	持股比例	认缴出资额	认缴出资日期	股东类型
        row = 1
        table.write(i, 0, i)
        table.write(i, 1, firm_name[i])
        table.write(i, 2, firm_address[i])
        table.write(i, 3, firm_key)

    file.save('vc_t2.xls')


if __name__ == '__main__':
    mainfunc()