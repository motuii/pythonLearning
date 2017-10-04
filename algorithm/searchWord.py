# -*- coding: utf-8 -*-

"""
__title__ = ''
__author__ = 'MoTuii'
__mtime__ = '2017/10/2'
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

word_map = {}
fo = open(r"D:\flipped.txt",'r')

for line in fo.readlines():
	for word in line.strip().split():
		# print word
		word_map[word] = word_map.get(word,0)+1

fo.close()
# print word_map

fo = open(r"D:\flipped_out.txt",'w')
for word,count in word_map.items():
	fo.write("{}  {}\n".format(word,count))
fo.close()