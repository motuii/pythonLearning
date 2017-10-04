#coding:utf-8

size = 7

for i in range(size):
	for j in range(size-i):
		if(i == 0 or j == 0 or j == size-i-1):
			print " *",
		else:
			print '  ',
	print
