# -*- coding: utf-8 -*-
import os
BOT_NAME = 'jdphone'

SPIDER_MODULES = ['jdphone.spiders']
NEWSPIDER_MODULE = 'jdphone.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# 主机环回地址
MONGODB_HOST = '127.0.0.1'
# 端口号，默认27017
MONGODB_POST = 27017
# 设置数据库名称
MONGODB_DBNAME = 'JingDong'
# 设置集合名称
MONGODB_COL = 'JingDongPhone'

# pipeline设置
ITEM_PIPELINES = {
    'jdphone.pipelines.JdphonePipeline': 300,
}