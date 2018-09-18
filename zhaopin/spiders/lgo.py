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
        kws = {'px': 'new', 'city': '上海', 'district': '浦东新区', 'bizArea': '', 'kd': '测试工程师'}
        px = kws['px']
        city = kws['city']
        district = kws['district']
        bizArea = kws['bizArea']
        kd = kws['kd']
        if district == '' and bizArea == '':
            url = f'https://www.lagou.com/jobs/positionAjax.json?px={px}&city={city}&needAddtionalResult=false'
            referer = f'https://www.lagou.com/jobs/list_{kd}?px={px}&city={city}'
        elif bizArea == '' and district != '':
            url = f'https://www.lagou.com/jobs/positionAjax.json?px={px}&city={city}&district={district}&needAddtionalResult=false'
            referer = f'https://www.lagou.com/jobs/list_{kd}?px={px}&city={city}&district={district}'
        else:
            url = f'https://www.lagou.com/jobs/positionAjax.json?px={px}&city={city}&district={district}&bizArea={bizArea}&needAddtionalResult=false'
            referer = f'https://www.lagou.com/jobs/list_{kd}?px={px}&city={city}&district={district}&bizArea={bizArea}'
        firLink = f'https://www.lagou.com/jobs/list_{kd}?px={px}&city={city}&district={district}&bizArea={bizArea}#order'
        firHds = {
            'Host': 'www.lagou.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Referer': referer.replace(f'{px}', 'default'),
            'Cookie': self.cookie,
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': 1
        }
        meta = {'px':px,'city':city,'district':district,'bizArea':bizArea,'kd':kd,'url':url,'referer':referer}
        yield Request(firLink,callback=self.pageCountList,headers=firHds,cookies=self.cookie,dont_filter=True,meta=meta)

    def pageCountList(self,response):   #获取页面数量和招聘页面列表
        count = int(response.xpath('//span[@class="span totalNum"]/text()')[0].extract())
        print(f'符合当前检索条件的页面共\033[1;33m{count}\033[0m页!')
        city = response.meta['city']
        kd = response.meta['kd']
        url = response.meta['url']
        referer = response.meta['referer']


        # kws={'px':'new','city':'上海','district':'浦东新区','bizArea':'','kd':'测试工程师'}
        # px = kws['px']
        # city = kws['city']
        # district = kws['district']
        # bizArea = kws['bizArea']
        # kd = kws['kd']
        # if district == '' and bizArea == '':
        #     url = f'https://www.lagou.com/jobs/positionAjax.json?px={px}&city={city}&needAddtionalResult=false'
        #     referer = f'https://www.lagou.com/jobs/list_{kd}?px={px}&city={city}'
        # elif bizArea == '' and district != '':
        #     url = f'https://www.lagou.com/jobs/positionAjax.json?px={px}&city={city}&district={district}&needAddtionalResult=false'
        #     referer = f'https://www.lagou.com/jobs/list_{kd}?px={px}&city={city}&district={district}'
        # else:
        #     url = f'https://www.lagou.com/jobs/positionAjax.json?px={px}&city={city}&district={district}&bizArea={bizArea}&needAddtionalResult=false'
        #     referer = f'https://www.lagou.com/jobs/list_{kd}?px={px}&city={city}&district={district}&bizArea={bizArea}'
        # firLink = f'https://www.lagou.com/jobs/list_{kd}?px={px}&city={city}&district={district}&bizArea={bizArea}#order'
        # firHds = {
        #     'Host': 'www.lagou.com',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        #     'Referer': referer.replace(f'{px}','default'),
        #     'Cookie':self.cookie,
        #     'Cache-Control': 'max-age=0',
        #     'Connection': 'keep-alive',
        #     'Upgrade-Insecure-Requests': 1
        # }
        for num in range(1,count+1):
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
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive'
            }
            meta = {'city': city, 'pn': num, 'kd': kd,'referer':referer}
            if num == 1:
                first = 'true'
            else:
                first = 'false'
            yield FormRequest(url=url,headers=hds,formdata={'first':first,'pn':f'{num}','kd':f'{kd}'},callback=self.parse,cookies=self.cookie,meta=meta,dont_filter=True)


    def parse(self, response):
        pn = response.meta['pn']
        referer =response.meta['referer']
        # print(response.text)
        isSuccess = json.loads(response.text)['success']
        if isSuccess == True:
            pgNo = json.loads(response.text)['content']['pageNo']
            if pgNo != 0:
                print(f'第{pn}页页面信息获取成功！')
            else:
                print(f'\033[1;31m ***Warning:第{pn}页页面信息获取失败！*** \033[0m')
                print(f'\033[1;31m {response.text} \033[0m')
                print('\033[1;31m可能的错误：\n1.district对应的bizArea不一致。\n2.没有更多页面！\033[0m')
                print('\033[1;31m {0} \033[0m \n'.format(30 * '*'))

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
            item['bizArea'] = response.xpath('string(//dd[@class="job-address clearfix"])')[0].extract().replace('查看地图', '').replace('工作地址','').strip().split('-')[2].strip()
            if item['bizArea'] == '':
                item['bizArea'] = None
            else:
                item['bizArea'] = item['bizArea']
        elif lenAdd ==3:
            item['district'] = response.xpath('string(//dd[@class="job-address clearfix"])')[0].extract().replace('查看地图', '').replace('工作地址', '').strip().split('-')[1].strip()
            item['bizArea'] = None
        else:
            item['district'] = None
            item['bizArea'] = None
        item['advantage'] = response.xpath('string(//dd[@class="job-advantage"])')[0].extract().replace('职位诱惑：','').strip()
        item['description'] = response.xpath('string(//dd[@class="job_bt"])')[0].extract().replace('职位描述：', '').strip().replace('\xa0','')
        item['address'] = response.xpath('//input[@name="positionAddress"]/@value')[0].extract()
        item['positionLng'] = response.xpath('//input[@name="positionLng"]/@value')[0].extract()
        item['positionLat'] = response.xpath('//input[@name="positionLat"]/@value')[0].extract()
        yield item






