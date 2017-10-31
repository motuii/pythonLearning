#coding:utf-8
import MySQLdb

db = MySQLdb.connect('localhost','root','root','bigdata')
cursor = db.cursor()

#插入
# sql = '''
# 	CREATE TABLE EMPLOYEE(
# 	FIRST_NAME CHAR(20) NOT NULL,
# 	LAST_NAME CHAR(20),
# 	AGE INT,
# 	SEX CHAR(1),
# 	INCOME FLOAT)'''

#查询
# try:
# 	sql = '''
# 		INSERT INTO EMPLOYEE(FIRST_NAME,
# 		LAST_NAME,AGE,SEX,INCOME)
# 		VALUES('APPLE','H',23,'M',96000)
# 		'''
# 	cursor.execute(sql)
# 	db.commit()
# except:
# 	db.rollback()
# 	print '出错了'

cursor.execute("select * from employee")
for i in range(cursor.rowcount):
	print cursor.fetchone()
db.close()
