class CZ(object):	
	def a():
		import pymysql
		db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
		cursor = db.cursor()
		q = int(input('请输入你想要查看的学生学号：'))
		sql = "SELECT * FROM xueji WHERE sno='%d'"%q
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				a = row[0]
				b = row[1]
				c = row[2]
				d = row[3]
				e = row[4]
				f = row[5]
				g = row[6]
				h = row[7]
				i = row[8]
				j = row[9]
				k = row[10]
				print('学生学号 = %d\n学生姓名 = %s\n学生性别 = %s\n学生年龄 = %d\n学生身份证号 = %s\n学生电话 = %s\n学生报考 = %s\n学生入学 = %s\n学生毕业 = %s\n学生学业 = %s\n学生备注 = %s\n'% \
					(a,b,c,d,e,f,g,h,i,j,k))
				db.commit()
		except:
			print('报错')
			db.rollback()
		db.close()

	def b():
		import pymysql
		db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
		cursor = db.cursor()
		q = int(input('请输入你想要查看的学生学号：'))
		sql = "SELECT * FROM tijian WHERE sno='%d'"%q
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				a = row[1]
				b = row[2]
				c = row[3]
				d = row[4]
				e = row[5]
				f = row[6]
				g = row[7]
				h = row[8]
				i = row[9]
				j = row[10]
				k = row[11]
				l = row[12]
				m = row[13]
				print('\n学生学号 = %d\n学生姓名 = %s\n学生身高 = %.1f\n学生体重 = %.1f\n学生颜色分辨 = %s\n学生左眼视力 = %.1f\n学生右眼视力 = %.1f\n学生左耳听力 = %s\n学生右耳听力 = %s\n学生双腿情况 = %s\n学生血压 = %s\n学生病史 = %s\n学生备注 = %s'% \
					(a,b,c,d,e,f,g,h,i,j,k,l,m))
				db.commit()
		except:
			print('报错')
			db.rollback()
		db.close()

	def c():
		import pymysql
		db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
		cursor = db.cursor()
		q = int(input('请输入你想要查看的学员学号：'))
		sql = "SELECT * FROM chengji WHERE sno='%d'"%q
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				a = row[1]
				b = row[2]
				c = row[3]
				d = row[4]
				e = row[5]
				f = row[6]
				print('\n学生编号 = %d\n学生姓名 = %s\n学生考试科目 = %d\n学生考试时间 = %s\n学生考试次数 = %d\n学生考试成绩 = %.1f'% \
					(a,b,c,d,e,f))
				db.commit()
		except:
			print('报错')
			db.rollback()
		db.close()

	def d():
		import pymysql
		db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
		cursor = db.cursor()
		q = int(input('请输入你想要查看的学生学号：'))
		sql = "SELECT * FROM lingzheng WHERE sno='%d'"%q
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				a = row[1]
				b = row[2]
				c = row[3]
				d = row[4]
				e = row[5]
				f = row[6]
				print('\n学生编号 = %d\n学生姓名 = %s\n学生驾驶证号 = %s\n学生领证时间 = %s\n学生驾驶证领取人 = %s\n学生备注 = %s'% \
					(a,b,c,d,e,f))
				db.commit()
		except:
			print('报错',e)
			db.rollback()
		db.close()

