#-*- coding: UTF-8 -*-

def swap(arr,i,j):
	arr[i],arr[j] = arr[j],arr[i]

arr=range(19)

for i in range(len(arr)/2):
	swap(arr,i,-i-1)
print arr