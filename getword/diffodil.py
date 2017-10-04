#-*- coding: UTF-8 -*-

"""
打印所以水仙花数，153是一个水仙花数，153=1***+5***+3***
"""

for i in range(100,1000):
	ge = i/100%10
	shi = i/10%10
	bai = i%10
	z = ge**3 + shi**3 + bai**3
	if (i==z):
		print i,
print

for x in range(1,10):
	for y in range(0,10):
		for z in range(0,10):
			n = x**3 + y**3 + z**3
			if n == x*100 +y*10 + z:
				print n,
