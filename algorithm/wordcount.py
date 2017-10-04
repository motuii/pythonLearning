# -*- coding: utf-8 -*-

"""
__title__ = ''
__author__ = 'MoTuii'
__mtime__ = '2017/10/3'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.

 ┏┓   ┏┓
┏┛┻━━━┛┻┓
┃   ☃   ┃
┃ ┳┛ ┗┳ ┃
┃   ┻   ┃
┗━┓   ┏━┛
  ┃   ┗━━━┓
  ┃神兽保佑 ┣┓
  ┃永无BUG！┏┛
  ┗┓┓┏━ ┳┓┏┛
   ┃┫┫  ┃┫┫
   ┗┻┛  ┗┻┛
"""
import re

dict1 = {}
path = r'D:\flipped.txt'
with open(path,'r') as fo:
	while True:
		line = fo.readline()
		if not line:break
		line = line.strip()
		if not line:continue
		words = re.compile("\W+").split(line)
		# print words
		for word in words:
			if word and len(word)>1:
				# print word
				dict1[word] = dict1.get(word,0)+1

# print dict1
item = dict1.items()

# 排序
item.sort(key=lambda x:x[1],reverse=True)

# 导入数据库
import MySQLdb

db = MySQLdb.connect("localhost","root","0618Qiaohui","bigdata")
cursor = db.cursor()

try:
	sql="insert into wordcount Values('%s',%d)"
	for k,v in item:
		sql_curr = sql % (k,v)
		print sql_curr
		cursor.execute(sql_curr)
	db.commit()
except v:
	print v
	db.rollback()
db.close()


















