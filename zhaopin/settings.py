# -*- coding: utf-8 -*-

# Scrapy settings for zhaopin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhaopin'

SPIDER_MODULES = ['zhaopin.spiders']
NEWSPIDER_MODULE = 'zhaopin.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#   'Accept': 'application/json, text/javascript, */*; q=0.01',
#   'X-Requested-With': 'XMLHttpRequest',
#   'Host': 'www.lagou.com',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'zhaopin.middlewares.ZhaopinSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'zhaopin.middlewares.ZhaopinDownloaderMiddleware': 200,
   # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':400,
   # 'zhaopin.middlewares.HttpProxyMiddleware':400,
   # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
   # 'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware':None
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhaopin.pipelines.ZhaopinPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#设置Cookie
# COOKIE = {'_ga': 'GA1.2.2138864544.1533631818',
#           'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1536634040,1536653812,1536730869,1536804703',
#           'user_trace_token': '20180807165100-01ebdef2-9a1f-11e8-a341-5254005c3644',
#           'LGUID': '20180807165100-01ebe1dd-9a1f-11e8-a341-5254005c3644',
#           'LG_LOGIN_USER_ID': '4044580018fedca9af00dfd183c448a8abc47cb79e14ec34a0d6b234cf2dae68',
#           'index_location_city': '%E4%B8%8A%E6%B5%B7',
#           '_gid': 'GA1.2.6003120.1536568128',
#           'showExpriedIndex': '1',
#           'showExpriedCompanyHome': '1',
#           'showExpriedMyPublish': '1',
#           'hasDeliver': '0',
#           'gate_login_token': '21fd8afbf4d9053962d27eb7c8d6c4e9c2cd76096623fe9a2de3917f5bc4c6d2',
#           'SEARCH_ID': 'a50d2f7c8b1e4cdf971e587f6e48e052',
#           'WEBTJ-ID': '20180913101142-165d0b2caca1a5-0c5be6b04e1d77-1161694a-2073600-165d0b2cacc371',
#           'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1536822858',
#           'LGRID': '20180913151426-a617a0f3-b724-11e8-95e8-525400f775ce',
#           '_putrc': '57BBA9EB292AEBD8123F89F2B170EADC',
#           'JSESSIONID': 'ABAAABAAAGFABEF7112ACB7BD42EE4044106DB1FA0D20EB',
#           'login': 'true',
#           'unick': 'CooperMin',
#           'TG-TRACK-CODE': 'search_code',
#           '_gat': '1',
#           'LGSID': '20180913151423-a4192bba-b724-11e8-b815-5254005c3644',
#           'PRE_UTM': '',
#           'PRE_HOST': '',
#           'PRE_SITE': 'https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Python%3F%26px%3Ddefault%26city%3D%25E4%25B8%258A%25E6%25B5%25B7',
#           'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Python%3Fpx%3Dnew%26city%3D%25E4%25B8%258A%25E6%25B5%25B7'}

COOKIE = {'_ga': 'GA1.2.2138864544.1533631818', 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1536730869,1536804703,1536891947,1537151709', 'user_trace_token': '20180807165100-01ebdef2-9a1f-11e8-a341-5254005c3644', 'LGUID': '20180807165100-01ebe1dd-9a1f-11e8-a341-5254005c3644', 'LG_LOGIN_USER_ID': '4044580018fedca9af00dfd183c448a8abc47cb79e14ec34a0d6b234cf2dae68', 'index_location_city': '%E4%B8%8A%E6%B5%B7', 'showExpriedIndex': '1', 'showExpriedCompanyHome': '1', 'showExpriedMyPublish': '1', 'hasDeliver': '0', 'gate_login_token': 'f6814577d7e83bc92d09d3aa2c62fa200a12a5538c5402ef76598b62adb6c168', 'JSESSIONID': 'ABAAABAAAGFABEF7D3D97474D79F7829367FFB32011E6BC', '_gat': '1', 'LGSID': '20180917103518-5129c141-ba22-11e8-a14b-525400f775ce', 'PRE_UTM': '', 'PRE_HOST': '', 'PRE_SITE': '', 'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F', 'LGRID': '20180917103527-565bfd30-ba22-11e8-a14b-525400f775ce', 'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1537151717', '_gid': 'GA1.2.2121851475.1537151709', '_putrc': '57BBA9EB292AEBD8123F89F2B170EADC', 'login': 'true', 'unick': 'CooperMin', 'TG-TRACK-CODE': 'index_navigation', 'SEARCH_ID': 'cfa638218dc24b4fa7498818c9147dd5', 'X_HTTP_TOKEN': '8b5c5ad8c19d4424756f2e8e29d7c32e'}

REDIRECT_ENABLE = False


#Mongo数据库
MG_HS = 'localhost'
MG_PR = 27017
MG_DB = 'zhaopin'
MG_COL = 'lgo'


#Mysql数据库
MS_HS = 'localhost'
MS_PR = 3306
MS_US = 'root'
MS_PD = 'admin'
MS_DB = 'recruit'
MS_TB = 'lgo'
