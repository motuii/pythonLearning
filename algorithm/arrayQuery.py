#-*- coding: UTF-8 -*-

arr = range(200)
m=40

def move(arr,m):
	return arr[len(arr)-m:len(arr)]+arr[0:len(arr)-m]
print move(arr,m)
