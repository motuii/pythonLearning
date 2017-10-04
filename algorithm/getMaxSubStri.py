#-*- coding: UTF-8 -*-

def getMaxSubString(str1,str2):
	maxStr = str1 if len(str1)>len(str2) else str2
	minStr = str2 if str1 == maxStr else str1
	flag = False
	result = []
	for i in range(len(minStr)):
		for j in range(i+1):
			subStr = str2[j:len(minStr)-i+j]
			if subStr in maxStr:
				result.append(subStr)
				flag = True
		if flag:break
	return result

str1 = "asdglewvnxmaie"
str2 = "asdfjglewxmai"
print getMaxSubString(str1,str2)