# -*- coding: utf-8 -*-
# @Author: IpomoeaAlba
# @Date:   2016-09-12 15:19:56
# @Last Modified by:   IpomoeaAlba
# @Last Modified time: 2016-09-13 01:11:56
import scrapy

class FundSpider(scrapy.Spider):
  name = 'fund'
  allowDomain = ['announce.fundclear.com.tw']
  start_urls = ['http://announce.fundclear.com.tw/MOPSFundWeb/D02_02.jsp']

  def parse(self, response):
          # filename = response.url.split('/')[-2] + '.html'
          # with open(filename, 'wb') as f:
          #     f.write(response.body)
    def post_data(self, response):
        print 'Preparing data'
        return [FormRequest.from_response(response,
                            formdata = {
                            'agentId': agentId,
                            'fundcomId': fundcomId,
                            'fundId': '123456'
                            },
                            callback = self.after_login
                            )]

