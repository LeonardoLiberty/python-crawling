# -*- coding: utf-8 -*-
import requests
import re
import time
import random
import math
import os
from lxml import etree
import xlrd
from selenium import webdriver


agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0)'
url = 'https://www.qichacha.com/search?key='
url2 = 'https://www.qichacha.com/firm_6a32ccc355c8e66df4f420e09a2bd06b.shtml'
headers = {
        "User-Agent": agent,
        'Cookie':'acw_tc=73e72d9515531600538066439e8652d01172ca8f303c7c4bb99867dbb6; QCCSESSID=6oqrbos8c1ib06qhjv0r6qt1t1; zg_did=%7B%22did%22%3A%20%221699f8da8a5f-0ea2421217fc5d-12666d4a-13c680-1699f8da8a61c4%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201553160054954%2C%22updated%22%3A%201553160158940%2C%22info%22%3A%201553160054959%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%222ccae7422e17e3bd5f508b3315848432%22%7D; UM_distinctid=1699f8daeb09b7-0968ee97c127e28-12666d4a-13c680-1699f8daeb1fc; CNZZDATA1254842228=181018681-1553159263-%7C1553159263; _uab_collina=155316005744353231354253; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1553160058; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1553160160'
            }
Shareholder_n = 0

def getrequest():
    try:
        result = requests.get("https://www.qichacha.com/search?key=浙江英联投资有限公司",headers=headers,timeout = 10).text
        #print(result)
        pattern = r'href="/firm_(.*?).html"'
        firm_code = re.findall(pattern, result, re.S)[0]
        print(firm_code)
    except Exception as e:
        print(e)


def getinfo():
    try:
        test = requests.get('https://www.qichacha.com/firm_'+'374f0ed27dad21c28e84e767b4a5439b'+'.html', headers=headers, timeout=20).text
        #print(test)
        #pattern = r'(.*?)'
        selector = etree.HTML(test)
        pattern2 = r'<meta name="author" content="leslie"> <title>(.*?)-'
        result_firm_name = re.findall(pattern2, test, re.S)[0]
        #base_info = selector.xpath('//section[starts-with(@class,"panel b-a base_info")]/div[@class="tcaption"]/h3[@class="title"] ')
        #num_name= selector.xpath('//div[@class="tcaption"]/')
        #name = selector.xpath('//h3[@class="seo font-14"]/text()')
        #// title[ @ lang]
        #/ html / body / div[4] / div[2] / div[1] / div / section[3] / table / tbody / tr[2] / td[
        #    2] / table / tbody / tr / td[2] / a / h3
        #result = base_info[0].xpath('string(.)')
        #result_name = name[:2]
        print(result_firm_name)

    except Exception as e:
        print(e)


def getnum_name():
    try:
        test = requests.get('https://www.qichacha.com/firm_' + '374f0ed27dad21c28e84e767b4a5439b' + '.html',
                            headers=headers, timeout=20).text
        # print(test)
        # pattern = r'(.*?)'
        selector = etree.HTML(test)
        pattern = r'股东信息</h3> <span class="tbadge">([0-9]{1,2})</span>'
        result_numname = re.findall(pattern, test, re.S)[0]

        print(result_numname)
    except Exception as e:
        print(e)

def get_name():
    try:
        test = requests.get('https://www.qichacha.com/firm_' + '374f0ed27dad21c28e84e767b4a5439b' + '.html',
                            headers=headers, timeout=20).text
        # print(test)
        # pattern = r'(.*?)'
        selector = etree.HTML(test)
        pattern2 = r'<h3 class="seo font-14">(.*?)</h3></a> <div class="m-t-xs"> '
        result_name = re.findall(pattern2, test, re.S)[:]
        print(result_name)
    except Exception as e:
        print(e)

def get_shrate():
    try:
        test = requests.get('https://www.qichacha.com/firm_' + '374f0ed27dad21c28e84e767b4a5439b' + '.html',
                            headers=headers, timeout=20).text
        # print(test)
        # pattern = r'(.*?)'
        selector = etree.HTML(test)
        pattern3 = r'<td class="text-center">\n                ([0-9].*?%)\n'
        result_name = re.findall(pattern3, test, re.S)[:]
        print(result_name)
    except Exception as e:
        print(e)

def get_shmoney():
    try:
        test = requests.get('https://www.qichacha.com/firm_' + '374f0ed27dad21c28e84e767b4a5439b' + '.html',
                            headers=headers, timeout=20).text
        # print(test)
        # pattern = r'(.*?)'
        selector = etree.HTML(test)
        pattern4 = r'<td class="text-center">\n                 \n                                                       (.*?)\n'
        result_name = re.findall(pattern4, test, re.S)[:]
        print(result_name)
    except Exception as e:
        print(e)

def get_date():
    try:
        test = requests.get('https://www.qichacha.com/firm_' + '374f0ed27dad21c28e84e767b4a5439b' + '.html',
                            headers=headers, timeout=20).text
        # print(test)
        # pattern = r'(.*?)'
        #section[3]/table/tbody/tr[2]/td[5]
        selector = etree.HTML(test)
        base_info = selector.xpath('//section[@class="panel b-a clear m_comInfoList"]/table//td[5]/text()')
        #date = base_info[0].xpath('/')
        #result = base_info.xpath('string(.)')
        #pattern5 = r'\n     (.*?) '
        #result_name = re.findall(pattern5, base_info, re.S)
        print(base_info)
    except Exception as e:
        print(e)
        
if __name__ == '__main__':     
    getrequest()
    getinfo()
    getnum_name()
    get_name()
    get_shrate()
    get_shmoney()
    get_date()

#搜到的公司名	股东	持股比例	认缴出资额	认缴出资日期	股东类型
#英联投资