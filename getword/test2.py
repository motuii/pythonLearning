#-*- coding: UTF-8 -*-
import chardet

fo = open("D:\\flipped.txt",'r')

dict1={}
for line in fo.readlines():
	for word in line.strip().split():
		dict1[word]=dict1.get(word,0)+1
fo.close()

fo = open("D:\\flipped2.txt",'w')
for word,count in dict1.items():
	fo.write("%s %s\n"%(word,count))
fo.close()