
from replay import *

import requests
from bs4 import BeautifulSoup
import urllib
import json
import time
from replay.utils import log

class LagouAPI(object):
    LAGOU_GATEWAY = 'http://www.lagou.com/jobs/positionAjax.json?'
    sess = requests.Session()

    @classmethod
    def search(cls, kd, **kwargs):
        # print(kwargs)
        # https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false
        """
        first:true
        pn:1
        kd:python
        """

        # 拼接url
        # urllib库里面有个urlencode函数，可以把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
        url_encoded = urllib.parse.urlencode(kwargs)
        jl_url = cls.LAGOU_GATEWAY + url_encoded
        print(jl_url)

        page = 1
        page_max = None
        while True:
            payload = {
                'pn': page,
                'kd':kd,
                'first': False,
            }
            print(payload)
            json_result = cls._db_h(jl_url, payload)
            log(json_result)
            if page_max is None:
                # 获得页数
                page_max = json_result['content']['positionResult']['totalCount']
                # # 119 
                if page_max > 10:
                    page_max = 10
                print(page_max)
            # 用生成器返回得到的结果
            result = json_result['content']['positionResult']['result']
            for j in result:
                yield j
                # cls.geo_info(j)
            if page >= page_max:
                break
            page += 1


    @classmethod
    def get_location_by_pos_id(cls, pos_id):
        r = cls.sess.get('http://www.lagou.com/jobs/{}.html'.format(pos_id))
        soup = BeautifulSoup(r.text, 'lxml')
        # log(soup)
        corp_info = soup.select('.work_addr')[0].get_text()
        corp_info = corp_info.strip().replace(' ','').replace('\n','')
        return corp_info

    @classmethod
    def _db_h(cls, jl_url, payload):
        """
        获取网络信息
        """
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
        }
        print("db ", payload)
        r = cls.sess.post(jl_url, headers=headers, data=payload)
        return r.json()

        # url = 'px=default&city={}&needAddtionalResult=false'.format(kwargs.get('city'))
        # cls.jl_url = cls.LAGOU_GATEWAY + url

        # wb_data = requests.post(cls.jl_url, data=payload).text
        # print(wb_data)
        # print(json_result)
    @classmethod
    def geo_info(cls, j):
        print('jj', j)
        d = dict(
            companyShortName = j['companyShortName'],
            # ctime = j['ctime']
            financeStage = j['financeStage'],
            workYear = j['workYear'],
            createTime = j['createTime'],
            positionLables = j['positionLables'],
            salary = j['salary'],
            businessZones = j['businessZones'],
            city = j['city'],
            positionName = j['positionName'],
            district = j['district'],
            companyLabelList = j['companyLabelList'],
            positionAdvantage = j['positionAdvantage'],
            jobNature = j['jobNature'],
            companySize = j['companySize'],
            industryField = j['industryField'],
            formatCreateTime = j['formatCreateTime'],
            education = j['education'],
            companyFullName = j['companyFullName'],
            companyLogo = j['companyLogo'],
            positionId = j['positionId'],
            companyId = j['positionId'],
        )
        compURL = 'https://www.lagou.com/jobs/{}.html'.format(d['companyId'])
        addr = cls.get_location_by_pos_id(d['positionId'])
        d['addr'] = addr
        d['compURL'] = compURL
        time.sleep(0.5)
        # print(addr, companyFullName, salary)
        return d