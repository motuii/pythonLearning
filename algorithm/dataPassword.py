#-*- coding: UTF-8 -*-

strnum = 1234

for i in str(strnum):
	print (int(i)+5)%10

l = [str((int(i)+5)%10) for i in str(strnum)]

print l

def f(i):
	return str((int(i)+5)%10)