#-*- coding: UTF-8 -*-


def isPrime(num):
	if (num >0):
		for i in range(2,num):
			if(num % i == 0):
				return False
		return True
	return False

result = []
for i in range(101,201):
	if(isPrime(i)):
		result.append(i)
print len(result),result

max = 100
result = []
src = range(2,max+1)

while len(src)>0:
	a = src.pop(0)
	for i in src:
		if (i%a == 0):
			src.remove(i)
	result.append(a)

print "素数个数为：%s，它们分别是：%s"%(len(result),result)