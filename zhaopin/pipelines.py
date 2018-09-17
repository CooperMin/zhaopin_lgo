# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from scrapy.conf import settings
import time


class ZhaopinPipeline(object):
    #该部分代码为连接MongoDB
    # def __init__(self):
    #     host = settings['MG_HS']
    #     port = settings['MG_PR']
    #     db = settings['MG_DB']
    #     col = settings['MG_COL']
    #     self.client = pymongo.MongoClient(host,port)
    #     self.db = self.client[db]
    #     self.col = self.db[col]
    #
    #
    # def process_item(self, item, spider):
    #     data = dict(item)
    #     try:
    #         self.col.insert(data)
    #         print('插入成功！')
    #     except:
    #         print('Error！')
    #     return item

    # 该部分代码为连接Mysql
    def __init__(self):
        host = settings['MS_HS']
        port = settings['MS_PR']
        user = settings['MS_US']
        passwd = settings['MS_PD']
        db = settings['MS_DB']
        self.client = pymysql.connect(
            host = host,
            port = port,
            user = user,
            passwd = passwd,
            db = db
        )
        self.cur = self.client.cursor()
        crt = """create table if not exists lgo(
                    `keyWord` varchar (32) default null comment'关键词',
                    `job` varchar (64) not null comment'职位',
                    `pubTime` varchar (32) default null comment'发布时间',
                    `city` varchar (32) not null comment'城市',
                    `district` varchar (32) not null comment'区县',
                    `street` varchar (32) not null comment'街道/社区',
                    `comName` varchar (128) default null comment'公司名称（简称/常用）',
                    `recDep` varchar (128) default null comment'公司名称（简称/常用）',
                    `salary` varchar (32) default null comment'薪资',
                    `experirence` varchar (32) default null comment'工作经验',
                    `education` varchar (32) default null comment'教育水平',
                    `workingMode` varchar (16) default null comment'工作方式',
                    `label` varchar (128) default null comment'标签',
                    `jobWelfare` varchar (256) default null comment'职位诱惑',
                    `jobDetail` text default null  comment'职位详情',
                    `comFamName` varchar (128) not null comment'公司名称（正式）',
                    `industry` varchar (64) default null comment'行业/领域',
                    `round` varchar (32) default null comment'融资轮次/发展阶段',
                    `scale` varchar (32) default null comment'公司规模',
                    `financeOrg` varchar (256) default null comment'投资机构',
                    `comPage` varchar (128) default null comment'公司主页',
                    `area` varchar (32) default null comment'地区/城市',
                    `address` varchar (128) default null comment'地址',
                    `zhaopinId` int (11) not null comment'招聘页面ID' primary key ,
                    `comId` int (8) not null comment'公司ID',
                    `userId` int (11) default null comment'HRID',
                    `phone` varchar (32) default null comment'手机号码',
                    `positionName` varchar (32) default null comment'职位名称', 
                    `receiveEmail` varchar (64) default null comment'接收邮箱',
                    `realName` varchar (32) default null comment'HR姓名',
                    `portrait` varchar (128) default null comment'公司logo',
                    `userLevel` varchar (32) default null comment'HR职级',
                    `canTalk` varchar (8) default null comment'交流意愿',
                    `isIdentify` varchar (16) default null comment'是否认证',
                    `writeTime` datetime not null comment'服务器时间/写入时间'
                )engine = innodb default charset=utf8 comment='拉勾招聘信息';"""
        self.cur.execute(crt)

    def process_item(self, item, spider):
        ins = """insert into lgo (`zhaopinId`,
                                  `userId`,
                                  `phone`,
                                  `positionName`,
                                  `receiveEmail`,
                                  `realName`,
                                  `portrait`,
                                  `userLevel`,
                                  `canTalk`,
                                  `jobWelfare`,
                                  `jobDetail`,
                                  `address`,
                                  `job`,
                                  `salary`,
                                  `area`,
                                  `experirence`,
                                  `education`,
                                  `workingMode`,
                                  `label`,
                                  `comId`,
                                  `writeTime`,
                                  `comFamName`,
                                  `comName`,
                                  `isIdentify`,
                                  `industry`,
                                  `round`,
                                  `scale`,
                                  `financeOrg`,
                                  `comPage`,
                                  `city`,
                                  `district`,
                                  `street`,
                                  `pubTime`,
                                  `keyWord`,
                                  `recDep`)
                        values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
                        """.format(item['zhaopinId'],
                                   item['userId'],
                                   item['phone'],
                                   item['positionName'],
                                   item['receiveEmail'],
                                   item['realName'],
                                   item['portrait'],
                                   item['userLevel'],
                                   item['canTalk'],
                                   item['jobWelfare'],
                                   item['jobDetail'],
                                   item['address'],
                                   item['job'],
                                   item['salary'],
                                   item['area'],
                                   item['experirence'],
                                   item['education'],
                                   item['workingMode'],
                                   item['label'],
                                   item['comId'],
                                   item['writeTime'],
                                   item['comFamName'],
                                   item['comName'],
                                   item['isIdentify'],
                                   item['industry'],
                                   item['round'],
                                   item['scale'],
                                   item['financeOrg'],
                                   item['comPage'],
                                   item['city'],
                                   item['district'],
                                   item['street'],
                                   item['pubTime'],
                                   item['keyWord'],
                                   item['recDep'])
        try:
            self.cur.execute(ins)
            self.client.commit()
            localTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            print(f'插入成功！(当前时间：{localTime})')
        except Exception as e:
            self.client.rollback()
            print('\n\033[1;31m{0} Warning：插入失败！ {0}\033[0m'.format(23*'+'))
            print('\033[1;31m{1}{0}{1} \033[0m'.format(e,6*'+'))
            print('\033[1;31m{0}\033[0m\n'.format(65*'+'))
        return item
    def spider_close(self,spider):
        self.client.close()