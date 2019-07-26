# -*- coding: utf-8 -*-
import os
BOT_NAME = 'jdphone'

SPIDER_MODULES = ['jdphone.spiders']
NEWSPIDER_MODULE = 'jdphone.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


MONGODB_HOST = '127.0.0.1'

MONGODB_POST = 27017

MONGODB_DBNAME = 'JingDong'

MONGODB_COL = 'JingDongPhone'

ITEM_PIPELINES = {
   'jdphone.pipelines.JdphonePipeline': 300,
}
