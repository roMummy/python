#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
from zipfile import ZipFile
from StringIO import StringIO
from downloader import Downloader
from link_crawler import link_crawler

# D = Downloader()
# zipped_data = D("http://s3.amazonaws.com/alexa-static/top-1m.csv.zip")
# urls = []
# with ZipFile(StringIO(zipped_data)) as zf:
# 	csv_filename = zf.namelist()[0]
# 	for _, website in csv.reader(zf.open(csv_filename)):
# 		urls.append("http://"+website)
class AlexaCallback:	
	"""docstring for AlexaCallback"""
	def __init__(self, max_urls=1000):
		self.max_urls = max_urls
		self.seed_url = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
	
	def __call__(self, url, html):
		if url == self.seed_url:
			urls = []
			with ZipFile(StringIO(html)) as zf:
				csv_filename = zf.namelist()[0]
				for _ in website in csv.reader(zf.open(csv_filename)):
					urls.append("http://" + website)
					if len(urls) == self.max_urls:
						break						
			return urls


scrape_callback = AlexaCallback()
link_crawler(seed_url=scrape_callback.seed_url, cache_callback=MongoCache(),scrape_callback=scrape_callback)