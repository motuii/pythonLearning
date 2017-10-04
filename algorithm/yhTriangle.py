#-*- coding: UTF-8 -*-
#Author Motuii
'''
 * ┏┓　　　┏┓ 
 * ┏┛┻━━━┛┻┓ 
 * ┃　　　　　　　┃ 　 
 * ┃　　　━　　　┃ 
 * ┃　┳┛　┗┳　┃ 
 * ┃　　　　　　　┃ 
 * ┃　　　┻　　　┃ 
 * ┃　　　　　　　┃ 
 * ┗━┓　　　┏━┛ 
 *  ┃　　　┃   神兽保佑　　　　　　　　　 
 *  ┃　　　┃   代码无BUG！ 
 *  ┃　　　┗━━━┓ 
 *  ┃　　　　　　　┣┓ 
 *  ┃　　　　　　　┏┛ 
 *  ┗┓┓┏━┳┓┏┛ 
 *    ┃┫┫　┃┫┫ 
 *    ┗┻┛　┗┻┛ 
 *  
 '''

n = 10
# arr = [[1]*i for i in range(1,n+1)]
# for i in range(len(arr)):
# 	for j in range(len(arr[i])):
# 		if (j!=0 and j!=len(arr[i-1])):
# 			arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
# 	print ' '.join(map(lambda x:str(x),arr[i]))

an = [1]*n
for i in range(n):
	for j in range(i-1,0,-1):
		an[j] = an[j]+an[j-1]

	print an[0:i+1]
	#print "\t".join(map(lambda x:str(x),an[0:i+1]))

