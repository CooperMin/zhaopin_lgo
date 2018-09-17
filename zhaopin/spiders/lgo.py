# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from scrapy import FormRequest,Request
from scrapy.conf import settings
import json
from zhaopin.items import ZhaopinItem
import time


class LgoSpider(scrapy.Spider):
    name = 'lgo'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']
    cookie = settings['COOKIE']

    def start_requests(self):
        kws={'city':'上海','district':'浦东新区','kd':'测试工程师'}
        city = kws['city']
        district = kws['district']
        kd = kws['kd']
        if district == '':
            url = f'https://www.lagou.com/jobs/positionAjax.json?px=new&city={city}&needAddtionalResult=false'
            referer = f'https://www.lagou.com/jobs/list_{kd}?px=new&city={city}'
        else:
            url = f'https://www.lagou.com/jobs/positionAjax.json?px=new&city={city}&district={district}&needAddtionalResult=false'
            referer = f'https://www.lagou.com/jobs/list_{kd}?px=new&city={city}&district={district}'
        for num in range(1,31):
            # referer = url.replace('&needAddtionalResult=false','')
            hds = {
                'Host': 'www.lagou.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Referer': referer,
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'X-Anit-Forge-Token': None,
                'X-Anit-Forge-Code': 0,
                # 'Content-Length': 27,
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive'
            }
            meta = {'city': city, 'pn': num, 'kd': kd,'referer':referer}
            yield FormRequest(url=url,headers=hds,formdata={'first':'false','pn':f'{num}','kd':f'{kd}'},callback=self.parse,cookies=self.cookie,meta=meta)


    def parse(self, response):
        pn = response.meta['pn']
        referer =response.meta['referer']
        print(response.text)
        isSuccess = json.loads(response.text)['success']
        if isSuccess == True:
            pgNo = json.loads(response.text)['content']['pageNo']
            if pgNo != 0:
                print(f'第{pn}页页面信息获取成功！')
            else:
                print(f'\033[1;31m ***Warning:第{pn}页获取失败！*** \033[0m')
                print(f'\033[1;31m {response.text} \033[0m')
                print('\033[1;31m {0} \033[0m \n'.format(30 * '*'))

            city = response.meta['city']
            pn = response.meta['pn']
            kd = response.meta['kd']
            recruitInfo = json.loads(response.text)['content']['hrInfoMap']
            for zhaopinId,comInfo in recruitInfo.items():
                item = ZhaopinItem()
                item['keyWord'] = kd
                item['zhaopinId'] = zhaopinId
                item['userId'] = comInfo['userId']
                item['phone'] = comInfo['phone']
                if comInfo['positionName'] != '':
                    item['positionName'] = comInfo['positionName']
                else:
                    item['positionName'] = None
                item['receiveEmail'] = comInfo['receiveEmail']
                item['realName'] = comInfo['realName']
                if comInfo['portrait'] is not None:
                    item['portrait'] = 'https://www.lgstatic.com/thumbnail_300x300/'+comInfo['portrait']
                else:
                    item['portrait'] = None
                item['userLevel'] = comInfo['userLevel']
                # if comInfo['canTalk'] == True:
                #     item['canTalk'] = 1
                # else:
                #     item['canTalk'] = 0
                item['canTalk'] = comInfo['canTalk']
                pageUrl = f'https://www.lagou.com/jobs/{zhaopinId}.html'
                hdsd = {
                    'Host': 'www.lagou.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                    'Referer': referer,
                    'Connection': 'keep-alive'
                }
                meta = {'item': item,'pn': pn}
                yield Request(url=pageUrl,callback=self.detail_parse,cookies=self.cookie,dont_filter=True,headers=hdsd,meta=meta)
        else:
            msg = print("\033[1;31m{0}\n+访问失败:{1}!+\n{0}\033[0m".format(32*'+',json.loads(response.text)['msg']))
            return msg

    def detail_parse(self,response):
        item = response.meta['item']
        pn = response.meta['pn']
        item['job'] = response.xpath('//div[@class="job-name"]/@title')[0].extract()
        item['recDep']= response.xpath('//div[@class="job-name"]/div[@class="company"]/text()')[0].extract()
        item['salary'] = response.xpath('//span[@class="salary"]/text()')[0].extract().strip()
        item['area'] = response.xpath('string(//dd[@class="job_request"]/p/span[2])')[0].extract().replace('/','').strip()
        item['experirence'] = response.xpath('string(//dd[@class="job_request"]/p/span[3])')[0].extract().replace('/','').strip()
        item['education'] = response.xpath('string(//dd[@class="job_request"]/p/span[4])')[0].extract().replace('/','').strip()
        item['workingMode'] = response.xpath('string(//dd[@class="job_request"]/p/span[5])')[0].extract().replace('/','').strip()
        labelList = response.xpath('//ul[@class="position-label clearfix"]/li/text()').extract()
        if str(labelList).replace('[','').replace(']','').replace("'","") == '':
            item['label'] = None
        else:
            item['label'] = str(labelList).replace('[','').replace(']','').replace("'","")
        item['comId'] = response.xpath('//div[@class="position-head"]/@data-companyid')[0].extract()
        serverTime = int(response.xpath('//input[@id="serverTime"]/@value')[0].extract())
        item['writeTime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(serverTime/1000))
        item['pubTime'] = response.xpath('string(//p[@class="publish_time"])')[0].extract().replace('\xa0','').strip()
        item['comFamName'] = response.xpath('//dl[@id="job_company"]/dt/a[@data-lg-tj-track-code="jobs_logo"]/img[@class="b2"]/@alt')[0].extract()
        item['comName'] = response.xpath('//dl[@id="job_company"]/dt/a[@data-lg-tj-track-code="jobs_logo"]/div/h2[@class="fl"]/text()')[0].extract().strip()
        item['isIdentify'] = response.xpath('//dl[@id="job_company"]/dt/a[@data-lg-tj-track-code="jobs_logo"]/div/h2[@class="fl"]/span[@class="dn"]/text()')[0].extract().strip()
        item['industry'] = response.xpath('string(//ul[@class="c_feature"]/li/span[text()="领域"]/parent::li)')[0].extract().replace('领域','').replace('\n','').strip()
        item['round'] = response.xpath('string(//ul[@class="c_feature"]/li/span[text()="发展阶段"]/parent::li)')[0].extract().replace('发展阶段','').strip()
        item['comPage'] = response.xpath('string(//ul[@class="c_feature"]/li/span[text()="公司主页"]/preceding-sibling::a)')[0].extract().replace(' 发展阶段','').replace('\n','').strip()
        item['financeOrg'] = response.xpath('string(//ul[@class="c_feature"]/li/span[text()="投资机构"]/parent::li)')[0].extract().replace('投资机构','').replace('\n','').strip()
        if item['financeOrg'] != '':
            item['financeOrg'] = item['financeOrg']
        else:
            item['financeOrg'] = None
        item['scale'] = response.xpath('string(//ul[@class="c_feature"]/li/span[text()="规模"]/parent::li)')[0].extract().replace('规模','').strip()
        item['city'] = response.xpath('//input[@name="workAddress"]/@value')[0].extract()
        lenAdd = len(response.xpath('string(//dd[@class="job-address clearfix"])')[0].extract().replace('查看地图', '').replace('工作地址','').strip().split('-'))
        if lenAdd == 4:
            item['district'] = response.xpath('string(//dd[@class="job-address clearfix"])')[0].extract().replace('查看地图', '').replace('工作地址','').strip().split('-')[1].strip()
            item['street'] = response.xpath('string(//dd[@class="job-address clearfix"])')[0].extract().replace('查看地图', '').replace('工作地址','').strip().split('-')[2].strip()
        else:
            item['district'] = None
            item['street'] = None
        item['jobWelfare'] = response.xpath('string(//dd[@class="job-advantage"])')[0].extract().replace('职位诱惑：','').strip()
        item['jobDetail'] = response.xpath('string(//dd[@class="job_bt"])')[0].extract().replace('职位描述：', '').strip().replace('\xa0','')
        item['address'] = response.xpath('//input[@name="positionAddress"]/@value')[0].extract()
        # item['address'] = response.xpath('string(//dd[@class="job-address clearfix"])')[0].extract().replace('查看地图', '').replace('工作地址','').strip().split('-')[-1].strip()
        # item['pn'] = pn
        # print(f"页码：{pn},{item['zhaopinId']},{item['userId']},{item['phone']},{item['positionName']}，{item['receiveEmail']},{item['realName']}，{item['portrait']},{item['receiveEmail']},{item['userLevel']},{item['userLevel']},{item['canTalk']},{item['job_welfare']},{item['job_detail']},{item['address']}")
        yield item




