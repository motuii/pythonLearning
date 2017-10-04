#-*- coding: UTF-8 -*-

list = [x*100+y*10+z*1 for x in range(1,5) for y in range(1,5) for z in range(1,5) if x!=y and y!=z and x!=z]
print len(list),list