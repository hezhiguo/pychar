#pymysql   是Python链接MySQL
import pymysql
#1.连接数据库
db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
#2.创建游标对象
cursor = db.cursor()

a = int(input('请输入科目号：'))
b = input('请输入科目名称：')
c = int(input('请输入先行考试科目：'))
sql = "INSERT INTO kemu values('%d','%s','%d')"%(a,b,c)
try:
	#正常
	cursor.execute(sql)
	db.commit()

except:
	print('报错')
	#错误
	db.rollback()
db.close()
