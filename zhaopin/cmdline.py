#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from scrapy import cmdline



cmdline.execute(['scrapy','crawl','lgo','-s','LOG_FILE= scrapy.log'])
# cmdline.execute(['scrapy','crawl','lgo'])
