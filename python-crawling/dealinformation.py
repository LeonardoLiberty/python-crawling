# -*- coding: utf-8 -*-
import requests
import re
import time
import random
import math
import os
from lxml import etree
import xlrd
def baseinformation(firmname,result_firm_name,selector):
    filename = 'baseinformation.txt'
    base_info = selector.xpath('//html/body/section[starts-with(@class,"panel b-a base_info")]')
    result = base_info[0].xpath('string(.)')
    result = re.sub(r'\n|\s|工商信息|对外投资与任职 >|查看地图|附近公司', '', result)
    result = re.sub(r'统一社会信用代码：', ']统一社会信用代码：', result)
    result = re.sub(r'纳税人识别号：', ']纳税人识别号：', result)
    result = re.sub(r'注册号：', ']注册号：', result)
    result = re.sub(r'组织机构代码：', ']组织机构代码：', result)
    result = re.sub(r'负责人：', ']负责人：', result)
    result = re.sub(r'法定代表人：', ']法定代表人：', result)
    result = re.sub(r'注册资本：', ']注册资本：', result)
    result = re.sub(r'经营状态：', ']经营状态：', result)
    result = re.sub(r'成立日期：', ']成立日期：', result)
    result = re.sub(r'公司类型：', ']公司类型：', result)
    result = re.sub(r'人员规模：', ']人员规模：', result)
    result = re.sub(r'营业期限：', ']营业期限：', result)
    result = re.sub(r'登记机关：', ']登记机关：', result)
    result = re.sub(r'核准日期：', ']核准日期：', result)
    result = re.sub(r'英文名：', ']英文名：', result)
    result = re.sub(r'所属地区', ']所属地区', result)
    result = re.sub(r'所属行业', ']所属行业', result)
    result = re.sub(r'企业地址：', ']企业地址：', result)
    result = re.sub(r'经营范围：', ']经营范围：', result)
    f = open(filename,'a',encoding='utf-8')
    f.write(firmname+']'+result_firm_name+']'+'基本信息'+']'+result)
    f.write('\n')
    f.close()
def Sockinfo(firmname,result_firm_name,selector):
    filename = 'Sockinfo.txt'
    f = open(filename,'a',encoding='utf-8')
    comInfolist = selector.xpath('//*[@id="Sockinfo"]/table/tr')
    for i in range(1,len(comInfolist)):
        result = ''
        all = comInfolist[i].xpath('td')
        for j in range(0,len(all)):
            text = all[j].xpath('string(.)')
            text = re.sub(r'\s|\n|对外投资与任职 >','',text)
            result = result +']'+text
        f.write(firmname+']'+result_firm_name+']'+'股东信息'+']'+result)
        f.write('\n')
    f.close()
def Mainmember(firmname,result_firm_name,selector):
    filename = 'Mainmember.txt'
    f = open(filename,'a',encoding = 'utf-8')
    mainmember = selector.xpath('//*[@id="Mainmember"][1]/table/tr')
    for i in range(1,len(mainmember)):
        result1 = mainmember[i].xpath('td')[0]
        result2 = mainmember[i].xpath('td')[1]
        member = result1.xpath('string(.)')
        member = re.sub(r'\s|\n|对外投资与任职 >','',member)
        job = result2.xpath('string(.)')
        job = re.sub(r'\s|\n','',job)
        f.write(firmname+']'+result_firm_name+']'+'主要成员'+']'+member+']'+job)
        f.write('\n')
def Changelist(firmname,result_firm_name,selector):
    #table_name = 'mistake'
    filename = 'changelist.txt'
    f = open(filename,'a',encoding='utf-8')
    changelist = selector.xpath('//*[@id="Changelist"]/table/tr')
    changelist_type ='变更类型'
    k = 1
    if k > len(changelist):
        print(firmname+'无变更记录')
        #print(content)
    while k < len(changelist):
        html = etree.tostring(changelist[k])
        if 'id="ma_twoword"' in str(html):
            changelist_type  = changelist[k].xpath('string(.)')
            k = k + 2
        else:
            all_result = changelist[k].xpath('td')
            result = ''
            for each in all_result:
                result0 = each.xpath('string(.)')
                result0 =re.sub(r'\s|\n|对外投资与任职>','',result0)
                result = result +']'+result0
            #print(result)
            f.write(firmname+']'+result_firm_name+']'+'变更记录'+']'+changelist_type+']'+result)
            f.write('\n')
            k = k+1
    f.close()
def Comintroduce(firmname,result_firm_name,selector):
    filename = 'Comintroduce.txt'
    f = open(filename, 'a', encoding='utf-8')
    comintroduce = selector.xpath('//*[@id="Comintroduce"]/div[2]')[0]
    result = comintroduce.xpath('string(.)')
    result = re.sub(r'\n|\s', '', result)
    #print(result)
    f.write(firmname + ']'+result_firm_name+']'+'简介'+']' + result)
    f.write('\n')
    f.close()
def Subcom(firmname,result_firm_name,selector):
    filename = 'Subcom.txt'
    f = open(filename, 'a', encoding='utf-8')
    subcom = selector.xpath('//*[@id="Subcom"]/div[2]/ul/li')
    for i in range(0, len(subcom)):
        result = subcom[i].xpath('string(.)')
        result = re.sub(r'\s|\n', ']', result)
        #print(result)
        f.write(firmname + ']'+result_firm_name+']'+'分支机构'+']' + result)
        f.write('\n')
    f.close()

# f = open('2333.txt',encoding= 'utf-8')
# content = f.read()
# #print(content)
# selector = etree.HTML(content)
# pattern = r'onclick="findRelation\(\'(.*?)\','
# result_firm_name = re.findall(pattern, content, re.S)[0]
# firm_name = 'a'
# Changelist('aa','22',selector)




data = xlrd.open_workbook("vc_test.xlsx")
table = data.sheets()[1]  # 0表示excel第一张sheet表
firm_name = table.col_values(1)  # 获取excel第一列中的所有值并保存为列表
firm_code = table.col_values(3)
new_firm_name =table.col_values(4)
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
headers = {
        "User-Agent": agent,
        'Cookie':'acw_tc=73e72d9515531600538066439e8652d01172ca8f303c7c4bb99867dbb6; QCCSESSID=6oqrbos8c1ib06qhjv0r6qt1t1; zg_did=%7B%22did%22%3A%20%221699f8da8a5f-0ea2421217fc5d-12666d4a-13c680-1699f8da8a61c4%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201553160054954%2C%22updated%22%3A%201553160158940%2C%22info%22%3A%201553160054959%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%222ccae7422e17e3bd5f508b3315848432%22%7D; UM_distinctid=1699f8daeb09b7-0968ee97c127e28-12666d4a-13c680-1699f8daeb1fc; CNZZDATA1254842228=181018681-1553159263-%7C1553159263; _uab_collina=155316005744353231354253; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1553160058; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1553160160'
}
for i in range(1,3):
    url = 'https://www.qichacha.com/company_getinfos?unique='+firm_code[i]+'&companyname='+firm_name[i]+'&tab=base'

    try:

        content = requests.get(url,headers=headers,timeout = 20).text
        selector = etree.HTML(content)
        pattern = r'onclick="findRelation\(\'(.*?)\','
        pattern2 = r'<meta name="author" content="leslie"> <title>(.*?)工商信息'
        result_firm_name = re.findall(pattern2, test, re.S)[0]
        #result_firm_name = new_firm_name[i]
        # if new_firm_name[i] in test:
        #     aaaa=2
        # else:
        #     print(ddd[9])
        #result_firm_name = ''
    except Exception as e:
        print(e)
        print(firm_name[i]+'出错----------------------------------')
        f= open('访问出错公司.txt','a',encoding='utf-8')
        f.write(firm_name[i]+' '+firm_code[i])
        f.write('\n')
        f.close()
        time.sleep(30)
        continue

    # try:
    #     baseinformation(firm_name[i],result_firm_name,selector)
    # except Exception as e:
    #     print(firm_name[i]+'无基本信息')
    # try:
    #     Sockinfo(firm_name[i], result_firm_name, selector)
    # except Exception as e:
    #     print(firm_name[i] + '无股东信息')
    # try:
    #     Mainmember(firm_name[i], result_firm_name, selector)
    # except Exception as e:
    #     print(firm_name[i] + '无主要成员信息')
    try:
        Changelist(firm_name[i], result_firm_name, selector)
    except Exception as e:
        print(firm_name[i] + '无变更记录')
    try:
        Subcom(firm_name[i], result_firm_name, selector)
    except Exception as e:
        print(firm_name[i] + '无分支机构')
    try:
        Comintroduce(firm_name[i], result_firm_name, selector)
    except Exception as e:
        print(firm_name[i] + '无公司简介')
    #print(firm_name[i] + '爬取成功')
    time.sleep(30)







