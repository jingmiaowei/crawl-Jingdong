# -*- coding: utf-8 -*-
import scrapy
from ..items import JdphoneItem
import sys


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']  
    keyword = "三星手机"
    page = 1
    url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%s&cid2=653&cid3=655&page=%d&click=0'
    next_url = 'https://search.jd.com/s_new.php?keyword=%s&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%s&cid2=653&cid3=655&page=%d&scrolling=y&show_items=%s'

    def start_requests(self):
        yield scrapy.Request(self.url % (self.keyword, self.keyword, self.page), callback=self.parse)

    def parse(self, response):
        """
        爬取每页的前三十个商品，数据直接展示在原网页中
        :param response:
        :return:
        """
        ids = []
        for li in response.xpath('//*[@id="J_goodsList"]/ul/li'):
            item = JdphoneItem()

            title = li.xpath('div/div/a/em/text()').extract()  
            price = li.xpath('div/div/strong/i/text()').extract()  
            comment_num = li.xpath('div/div/strong/a/text()').extract()  
            id = li.xpath('@data-pid').extract()  
            ids.append(''.join(id))

            url = li.xpath('div/div[@class="p-name p-name-type-2"]/a/@href').extract()  

            item['title'] = ''.join(title)
            item['price'] = ''.join(price)
            item['comment_num'] = ''.join(comment_num)
            item['url'] = ''.join(url)

            if item['url'].startswith('//'):
                item['url'] = 'https:' + item['url']
            elif not item['url'].startswith('https:'):
                item['info'] = None
                yield item
                continue

            yield scrapy.Request(item['url'], callback=self.info_parse, meta={"item": item})

        headers = {'referer': response.url}
        # 后三十页的链接访问会检查referer，referer是就是本页的实际链接
        # referer错误会跳转到：https://www.jd.com/?se=deny
        self.page += 1
        yield scrapy.Request(self.next_url % (self.keyword, self.keyword, self.page, ','.join(ids)),
                             callback=self.next_parse, headers=headers)

    def next_parse(self, response):
        """
        爬取每页的后三十个商品，数据展示在一个特殊链接中：url+id(这个id是前三十个商品的id)
        :param response:
        :return:
        """
        for li in response.xpath('//li[@class="gl-item"]'):
            item = JdphoneItem()
            title = li.xpath('div/div/a/em/text()').extract()  
            price = li.xpath('div/div/strong/i/text()').extract()  
            comment_num = li.xpath('div/div/strong/a/text()').extract()  
            url = li.xpath('div/div[@class="p-name p-name-type-2"]/a/@href').extract()  

            item['title'] = ''.join(title)
            item['price'] = ''.join(price)
            item['comment_num'] = ''.join(comment_num)
            item['url'] = ''.join(url)

            if item['url'].startswith('//'):
                item['url'] = 'https:' + item['url']
            elif not item['url'].startswith('https:'):
                item['info'] = None
                yield item
                continue

            yield scrapy.Request(item['url'], callback=self.info_parse, meta={"item": item})

        if self.page < 200:
            self.page += 1
            yield scrapy.Request(self.url % (self.keyword, self.keyword, self.page), callback=self.parse)

    def info_parse(self, response):
        """
        链接跟进，爬取每件商品的详细信息,所有的信息都保存在item的一个子字段info中
        :param response:
        :return:
        """
        item = response.meta['item']
        item['info'] = {}
        type = response.xpath('//div[@class="inner border"]/div[@class="head"]/a/text()').extract()
        name = response.xpath('//div[@class="item ellipsis"]/text()').extract()
        item['info']['type'] = ''.join(type)
        item['info']['name'] = ''.join(name)

        for div in response.xpath('//div[@class="Ptable"]/div[@class="Ptable-item"]'):
            h3 = ''.join(div.xpath('h3/text()').extract())
            if h3 == '':
                h3 = "未知"
            dt = div.xpath('dl/dl/dt/text()').extract()
            dd = div.xpath('dl/dl/dd[not(@class)]/text()').extract()
            item['info'][h3] = {}
            for t, d in zip(dt, dd):
                item['info'][h3][t] = d
        yield item
    
