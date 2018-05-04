class TJ(object):
	def a():
		import pymysql
		db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
		cursor = db.cursor()
		a = int(input('请输入学生学号：'))
		b = input('请输入学生姓名：')
		c = input('请输入学生性别(男、女)：')
		d = int(input('请输入学生年龄：'))
		e = input('请输入学生身份证号：')
		f = input('请输入学生电话：')
		# g = input('请输入学生报考车型：')
		h = input('请输入学生入学时间：')
		i = input('请输入学生毕业时间：')
		j = input('请输入学生学业状态(毕业、学习中、退学)：')
		k = input('请输入学员备注：')
		sql = "INSERT INTO xueji values('%d','%s','%s','%d','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,h,i,j,k)
		try:
			cursor.execute(sql)
			db.commit()
			print('添加成功')
		except:
			print('报错')
			db.rollback()
		db.close()

	def b():
		import pymysql
		db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
		cursor = db.cursor()
		a = int(input('请输入学生学号：'))
		b = input('请输入学生姓名：')
		c = float(input('请输入学生身高：'))
		d = float(input('请输入学生体重：'))
		e = input('请输入学生颜色分辨(正常,色弱,色盲)：')
		f = float(input('请输入学生左眼视力(1.0~5.5)：'))
		g = float(input('请输入学生右眼视力(1.0~5.5)：'))
		h = input('请输入学生左眼听力(正常,偏弱)：')
		i = input('请输入学生右眼听力(正常,偏弱)：')
		j = input('请输入学生腿长是否相等(正常,不相等)：')
		k = input('请输入学生血压情况(正常,偏高,偏低)：')
		l = input('请输入学生病史：')
		m = input('请输入学生备注：')
		sql = "INSERT INTO tijian values(0,'%d','%s','%f','%f','%s','%f','%f','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,g,h,i,j,k,l,m)
		try:
			cursor.execute(sql)
			db.commit()
		except:
			print('报错')
			db.rollback()
		db.close()

	def c():
		import pymysql
		db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
		cursor = db.cursor()
		a = int(input('请输入学号：'))
		b = int(input('请输入科目号：'))
		c = input('请输入考试时间：')
		d = int(input('请输入考试次数：'))
		e = float(input('请输入成绩：'))
		sql = "INSERT INTO chengji values(0,'%d','%d','%s','%d','%1f')"%(a,b,c,d,e)
		try:
			cursor.execute(sql)
			db.commit()
		except:
			print('报错')
			db.rollback()
		db.close()

	# def d():
	# 	import pymysql
	# 	db = pymysql.connect('localhost','root','asdasd','jiaxiao',charset='utf8')
	# 	cursor = db.cursor()
	# 	a = int(input('请输入学号：'))
	# 	b = input('请输入姓名：')
	# 	c = input('请输入驾驶证号：')
	# 	d = input('请输入领证时间：')
	# 	e = input('请输入领证人：')
	# 	f = input('请输入备注：')
	# 	sql = "INSERT INTO lingzheng values(0,'%d','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f)
	# 	try:
	# 		cursor.execute(sql)
	# 		db.commit()
	# 	except:
	# 		print('报错')
	# 		db.rollback()
	# 	db.close()

