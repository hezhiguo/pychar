class SC(object):
	def a():	
		import pymysql
		db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
		cursor = db.cursor()
		a = int(input('请输入你想要删除的学生学号：'))
		sql = "DELETE FROM xueji WHERE sno='%d'"%(a)
		try:
			cursor.execute(sql)
			db.commit()

		except:
			print('报错')
			db.rollback()
		db.close()

		print('删除成功')

	def b():
		import pymysql
		db = pymysql.connect('localhost','root','asdasd','jiaxiao',charset='utf8')
		cursor = db.cursor()
		a = int(input('请输入你想要删除的学员学号：'))
		sql = "DELETE FROM tijian WHERE sno='%d'"%(a)
		try:
			cursor.execute(sql)
			db.commit()

		except:
			print('报错')
			db.rollback()
		db.close()

		print('删除成功')

	def c():
		import pymysql
		db = pymysql.connect('localhost','root','asdasd','jiaxiao',charset='utf8')
		cursor = db.cursor()
		a = int(input('请输入你想要删除的学员学号：'))
		sql = "DELETE FROM chengji WHERE Sno='%d'"%(a)
		try:
			cursor.execute(sql)
			db.commit()
		except:
			print('报错')
			db.rollback()
		db.close()

		print('删除成功')

	def d():
		import pymysql
		db = pymysql.connect('localhost','root','asdasd','jiaxiao',charset='utf8')
		cursor = db.cursor()
		a = int(input('请输入你想要删除的学员学号：'))
		sql = "DELETE FROM lingzheng WHERE sno='%d'"%(a)
		try:
			cursor.execute(sql)
			db.commit()

		except:
			print('报错')
			db.rollback()
		db.close()

		print('删除成功')