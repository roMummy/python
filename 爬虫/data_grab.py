#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from bs4 import BeautifulSoup
# from download_test import download
from download_test import link_crawler
import downloader
import lxml.html
import lxml.cssselect
import csv
import urlparse

FIELDS = ("area", "iso", "tld")


#正则表达式  使用正则表达式获取数据的方式，健壮性不够,不容易理解
url = "http://example.webscraping.com/places/default/view/Algeria-4"
# html = download(url, {}, None, 2)
# re_message = re.findall('<td class="w2p_fw">(.*?)</td>', html)
# print(re_message)

#Beautiful Soup 速度慢

# broken_html = '<ul class=country><li>Area<li>Population</ul>'
# soup = BeautifulSoup(broken_html, 'html.parser')
# #美化
# fixed_html = soup.prettify()
# print(fixed_html)

# ul = soup.find("ul", attrs={"class":"country"})
# ul.find("li")
# print(ul.find_all("li"))

# soup = BeautifulSoup(html, "html.parser")
# tr = soup.find(attrs={"id":"places_area__row"})
# td = tr.find(attrs={"class":"w2p_fw"})
# area = td.text
# print(area)

#Lxml 速度比Beautiful Soup快

# broken_html = '<ul class=country><li>Area<li>Population</ul>'
# tree = lxml.html.fromstring(broken_html)
# fixed_html = lxml.html.tostring(tree, pretty_print=True)
# print(fixed_html)

# tree = lxml.html.fromstring(html)
# print(type(tree))
 
# td = tree.cssselect("tr#places_area__row > td.w2p_fw")[0]
# area = td.text_content()
# print(area)

#链接回调 
# def scrape_callback(url, html):
# 	if re.search("/view/",url):
# 		tree = lxml.html.fromstring(html)
# 		row = [tree.cssselect("table > tr#places_area__row > td.w2p_fw")[0].text_content]
# 		print(url, row)


#将下载的数据存入到表格中
# class ScrapeCallBack():
# 	def __init__(self):
# 		self.writer = csv.writer(open("countries.csv", "w"))
# 		self.fields = ("area", "iso", "country")
# 		self.writer.writerow(self.fields)

# 	def __call__(self, url, html):
# 		if re.search("/view/",url):
# 			tree = lxml.html.fromstring(html)
# 			row = []
# 			for field in self.fields:
# 				row.append(tree.cssselect("table > tr#places_{}__row > td.w2p_fw".format(field))[0].text_content)
# 			self.writer.writerow(row)

# link_crawler("http://example.webscraping.com/places/default/view/Algeria-4",  '/(index|view)', max_depth=-1, scrape_callback=ScrapeCallBack())


#磁盘保存
components = urlparse.urlsplit("http://example.webscraping.com/places/default/view/Algeria-4/")
print(components)
path = components.path
if not path:
	path = "/index.html"
elif path.endswith("/"):
	path += "index.html"
filename = components.netloc + path + components.query
print(filename)
