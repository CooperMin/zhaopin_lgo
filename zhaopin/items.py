# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zhaopinId = scrapy.Field()      #(1)招聘页面ID
    userId = scrapy.Field()         #(2)HRID
    phone = scrapy.Field()          #(3)手机号码
    positionName = scrapy.Field()   #(4)职位名称
    receiveEmail = scrapy.Field()   #(5)接收邮箱
    realName = scrapy.Field()       #(6)HR姓名
    portrait = scrapy.Field()       #(7)公司logo
    userLevel = scrapy.Field()      #(8)HR职级
    canTalk = scrapy.Field()        #(9)交流意愿
    advantage = scrapy.Field()      #(10)职位诱惑
    description = scrapy.Field()    #(11)职位描述/详情
    address = scrapy.Field()        #(12)地址
    # pn = scrapy.Field()             #(13)页码
    job = scrapy.Field()            #(14)职位
    salary = scrapy.Field()         #(15)薪资
    area = scrapy.Field()           #(16)地区/城市
    experirence = scrapy.Field()    #(17)工作经验
    education = scrapy.Field()      #(18)教育水平
    workingMode = scrapy.Field()    #(19)工作方式
    label = scrapy.Field()          #(20)标签
    comId = scrapy.Field()          #(21)公司ID
    writeTime = scrapy.Field()      #(22)服务器时间/写入时间
    comFamName = scrapy.Field()     #(23)公司名称（正式）
    comName = scrapy.Field()        #(24)公司名称（简称/常用）
    isIdentify = scrapy.Field()     #(25)是否认证
    industry = scrapy.Field()       #(26)行业/领域
    round = scrapy.Field()          #(27)融资轮次/发展阶段
    scale = scrapy.Field()          #(28)公司规模
    financeOrg = scrapy.Field()     #(29)投资机构
    comPage = scrapy.Field()        #(30)公司主页
    city = scrapy.Field()           #(31)城市
    district = scrapy.Field()       #(32)区县
    bizArea = scrapy.Field()        #(33)街道/社区
    pubTime = scrapy.Field()        #(34)发布时间
    keyWord = scrapy.Field()        #(35)关键词
    recDep = scrapy.Field()         #(36)招聘部门
    positionLng = scrapy.Field()    #(37)经度坐标
    positionLat = scrapy.Field()    #(38)纬度坐标




