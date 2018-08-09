#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import urlparse
import pickle
import zlib
from link_crawler import link_crawler
from detetime import datetime, timedelta


class DiskCache:
	"""docstring for DiskCache"""
	def __init__(self, cache_dir="cache", expires=timedelta(days=30)):
		self.cache_dir = cache_dir		
		self.expires = expires
	#保存到本地中
	def url_to_path(self, url):
		components = urlparse.urlsplit(url)
		path = components.path
		if not path:
			path = "/index.html"
		elif path.endswith("/"):
			path += "index.html"
		filename = components.netloc + path + components.query
		filename = re.sub("[^/0-9a-zA-Z\-.,;_]", "_", filename)
		filename = "/".join(segment[:255] for segment in filename.split("/"))
		return os.path.join(self.cache_dir, filename)

	def __getitem__(self, url):
		path = self.url_to_path(url)
		if os.path.exists(path):
			with open(path, "rb") as fp:
				result, timestamp = pickle.loads(zlib.decompress(fp.read()))
				if self.has_expired(timestamp):
					raise KeyError(url + " has expired")
					
				return result
		else:
			raise KeyError(url + "does not exist")
	
	def __setitem__(self, url, result):
		path = self.url_to_path(url)
		folder = os.path.dirname(path)
		if not os.path.exists(folder):
			os.makedirs(folder)
   		timestamp = datetime.utcnow()
   		data = pickle.dumps((result, timestamp))
		with open(path, "wb") as fp:
			#压缩并保存到本地
			fp.write(zlib.compress(pickle.dump(result))


	def has_expired(self, timestamp):
		return datetime.utcnow() > timestamp + self.expires
		
# if __name__ == '__main__':
#     link_crawler('http://example.webscraping.com/', '/(index|view)', cache=DiskCache())


