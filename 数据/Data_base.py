#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
import json
import sys
import re

# from xml.etree import ElementTree as ET

#########CSV 逗号分隔符

#导入CSV数据
# csvfile = open("data-text.csv", "r")
# reader = csv.DictReader(csvfile)
# print(reader)
# for row in reader:
# 	print(row)

# #导入json数据
# json_data = open("data_text.json").read()
# data = json.loads(json_data)
# print(data)
# for item in data:
# 	print(item)

# #导入xml数据
# tree = ET.parse("data-text.xml")
# root = tree.getroot()

# xml_data = root.find("Data")
# all_data = []

# print(dir(root))
# print(list(root))
texts = open("moviedialog.txt").read()
regex_str="[\u4e00-\u9fa5]"
# new_texts = re.findall(regex_str, texts)
for line in texts:
	new_text = re.findall(regex_str, texts)
	print(new_text)