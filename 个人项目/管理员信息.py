#pymysql   是Python链接MySQL
import pymysql
#1.连接数据库
db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
#2.创建游标对象
cursor = db.cursor()

a = str(input('请输入你注册的用户名：'))
b = str(input('请输入你的密码：'))
sql = "INSERT INTO guanliyuan values('%s','%s')"%(a,b)
try:
	#正常
	cursor.execute(sql)
	db.commit()

except:
	print('报错')
	#错误
	db.rollback()
db.close()

print('注册成功')