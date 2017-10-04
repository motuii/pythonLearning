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

a = [1, 3, 45, 7, 57, 23, 43, 65, 82, 16, 10, 91, 32]
a.sort()
print a

# key = raw_input("请输入要查找的值：\n")

# for i in range(len(a)):
# 	if (a[i] == key) :
# 		print "已找到：",i+1
# 		break
# else:
# 	print "没有找到"

def binarySearch(arr,key):
	left = 0
	right = len(a) - 1
	mid = 0
	# print right,mid
	while left <= right:
		mid = (left + right) / 2
		if (arr[mid] == key):
			return mid, a[mid]
		elif (arr[mid] > key):
			right = mid - 1
		elif (arr[mid] < key):
			left = mid + 1
	else:
		return -mid-1


print binarySearch(a,key=16)
print binarySearch(a,key=100)









