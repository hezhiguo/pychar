class XG(object):
	def a():
		import pymysql
		db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
		cursor = db.cursor()
		print('请问你想修改什么内容')
		q = str(input('修改学生名字:1\n修改学生性别:2\n修改学生年龄:3\n修改学生身份证号:4\n修改学生电话:5\n修改学生报考信息:6\n修改学生入学时间:7\n修改学生学业情况:8\n修改学生备注:9\n修改全部:10\n您想修改：'))
		if q == '1':
			a = input('修改的名字：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE xueji SET name='%s' WHERE sno='%d' "%(a,b)
		elif q == '2':	
			a = input('修改的性别：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE xueji SET sex='%s' WHERE sno='%d' "%(a,b)
		elif q == '3':	
			a = int(input('修改的年龄：'))
			b = int(input('修改的学生编号：'))
			sql = "UPDATE xueji SET age='%d' WHERE sno='%d' "%(a,b)
		elif q == '4':	
			a = input('修改的身份证号：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE xueji SET identify='%s' WHERE sno='%d' "%(a,b)
		elif q == '5':	
			a = input('修改的电话：')
			b = int(input('修改的学员编号：'))
			sql = "UPDATE xueji SET tell='%s' WHERE sno='%d' "%(a,b)
		elif q == '6':	
			a = input('修改的报考信息：')
			b = int(input('修改的学员编号：'))
			sql = "UPDATE xueji SET car_type='%s' WHERE sno='%d' "%(a,b)
		elif q == '7':	
			a = input('修改的入学时间：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE xueji SET ruxue_time='%s' WHERE sno='%d' "%(a,b)
		# elif q == '8':	
		# 	a = input('修改的毕业时间：')
		# 	b = int(input('修改的学员编号：'))
		# 	sql = "UPDATE xueji SET biye_time='%s' WHERE sno='%d' "%(a,b)
		elif q == '8':	
			a = input('修改的学业状况(毕业，学习中，退学)：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE xueji SET stondition='%s' WHERE sno='%d' "%(a,b)
		elif q == '9':	
			a = input('修改的备注：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE xueji SET s_text='%s' WHERE sno='%d' "%(a,b)
		elif q == '10':	
			a = input('修改的姓名：')
			b = input('修改的性别(男、女)：')
			c = int(input('修改的年龄：'))
			d = input('修改的身份证号：')
			e = input('修改的电话：')
			f = input('修改的报考车型：')
			g = input('修改的入学时间：')
			h = input('修改的毕业时间：')
			i = input('修改的学业状态(毕业、学习中、退学)：')
			j = input('修改的备注：')
			k = int(input('想要修改的学生编号：：'))
			sql = "UPDATE xueji SET name='%s',sex='%s',age='%d',identify='%s',tell='%s',car_type='%s',ruxue_time='%s',biye_time='%s',stondition='%s',s_text='%s' WHERE sno='%d' "%(a,b,c,d,e,f,g,h,i,j,k)
		else:
			exit()
		try:
			cursor.execute(sql)
			db.commit()
		except:
			print('报错')
			db.rollback()
		db.close()
		print('更改成功')

	def b():
		import pymysql
		db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
		cursor = db.cursor()
		print('请问你想修改什么内容')
		q = str(input('修改学生名字:1\n修改学生身高:2\n修改学生体重:3\n修改学生颜色分辨情况:4\n修改学生左眼视力:5\n修改学生右眼视力:6\n修改学生左耳听力:7\n修改学生右耳听力:8\n修改学生双腿情况:9\n修改学生血压情况:10\n修改学生病史:11\n修改学生备注:12\n修改全部:13\n您想修改：'))
		if q == '1':
			a = input('修改的学生名字：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE tijian SET name='%s' WHERE sno='%d' "%(a,b)
		elif q == '2':	
			a = input('修改的学生身高：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE tijian SET height='%.1f' WHERE sno='%d' "%(a,b)
		elif q == '3':	
			a = int(input('修改的学生体重：'))
			b = int(input('修改的学生编号：'))
			sql = "UPDATE tijian SET weight='%.1f' WHERE sno='%d' "%(a,b)
		elif q == '4':	
			a = input('修改的学生颜色分辨情况：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE tijian SET differentiate='%s' WHERE sno='%d' "%(a,b)
		elif q == '5':	
			a = input('修改的学生左眼视力：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE tijian SET left_sight='%.1f' WHERE sno='%d' "%(a,b)
		elif q == '6':	
			a = input('修改的学生右眼视力：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE tijian SET rigeht_sight='%.1f' WHERE sno='%d' "%(a,b)
		elif q == '7':	
			a = input('修改的学生左耳听力(正常,偏弱)：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE tijian SET left_ear='%s' WHERE sno='%d' "%(a,b)
		elif q == '8':	
			a = input('修改的学生右耳听力(正常,偏弱)：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE tijian SET right_ear='%s' WHERE sno='%d' "%(a,b)
		elif q == '9':	
			a = input('修改的学生双腿情况(正常,不相等)：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE tijian SET legs='%s' WHERE sno='%d' "%(a,b)
		elif q == '10':	
			a = input('修改的学生血压情况(正常,偏低,偏高)：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE tijian SET pressure='%s' WHERE sno='%d' "%(a,b)
		elif q == '11':	
			a = input('修改的学生病史：')
			b = int(input('修改的学员编号：'))
			sql = "UPDATE tijian SET history='%s' WHERE sno='%d' "%(a,b)
		elif q == '12':	
			a = input('修改的学生备注：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE tijian SET h_text='%s' WHERE sno='%d' "%(a,b)
		elif q == '13':	
			a = input('修改的学生姓名：')
			c = float(input('修改的学生身高：'))
			d = float(input('修改的学生体重：'))
			e = input('修改的学生颜色分辨情况(正常,色弱,色盲)：')
			f = float(input('修改的学生左眼视力：'))
			g = float(input('修改的学生右眼视力：'))
			h = input('修改的学生左耳听力(正常,偏低)：')
			i = input('修改的学生右耳听力(正常,偏低)：')
			j = input('修改的学生腿长情况(正常,不相等)：')
			k = input('修改的学生血压(正常,偏低,偏高)：')
			l = input('修改的学生病史：')
			m = input('修改的学生备注：')
			n = int(input('想要修改的学生编号：'))
			sql = "UPDATE tijian SET name='%s',height='%.1f',weight='%.1f',differentiate='%s',left_sight='%.1f',rigeht_sight='%.1f',left_ear='%s',right_ear='%s',legs='%s',pressure='%s',history='%s',h_text'%s' WHERE sno='%d' "%(a,c,d,e,f,g,h,i,j,k,l,m,n)
		else:
			exit()

		try:
			cursor.execute(sql)
			db.commit()
		except:
			print('报错')
			db.rollback()
		db.close()
		print('更改成功')

	def c():
		import pymysql
		db = pymysql.connect('localhost','root','bc123','school',charset='utf8')
		cursor = db.cursor()
		print('请问你想修改什么内容')
		q = str(input('修改学生名字:1\n修改学生考试科目:2\n修改学生考试时间:3\n修改学生考试次数:4\n修改学生考试成绩:5\n修改全部:6\n您想修改：'))
		if q == '1':
			a = input('修改的学生名字：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE chengji SET name='%s' WHERE Sno='%d' "%(a,b)
		elif q == '2':	
			a = int(input('修改的学生考试科目：'))
			b = int(input('修改的学生编号：'))
			sql = "UPDATE chengji SET cno='%d' WHERE Sno='%d' "%(a,b)
		elif q == '3':	
			a = input('修改的学生考试时间：')
			b = int(input('修改的学生编号：'))
			sql = "UPDATE chengji SET kaoshi_time='%s' WHERE Sno='%d' "%(a,b)
		elif q == '4':	
			a = int(input('修改的学生考试次数：'))
			b = int(input('修改的学生编号：'))
			sql = "UPDATE chengji SET times='%d' WHERE Sno='%d' "%(a,b)
		elif q == '5':	
			a = float(input('修改的学生考试成绩：'))
			b = int(input('修改的学生编号：'))
			sql = "UPDATE chengji SET scores='%.1f' WHERE Sno='%d' "%(a,b)
		elif q == '6':	
			a = input('修改的学生姓名：')
			b = int(input('修改的学生考试科目：'))
			c = input('修改的学生考试时间：')
			d = int(input('修改的学生考试次数：'))
			e = float(input('修改的学生考试成绩：'))
			f = int(input('想要修改的学生编号：'))
			sql = "UPDATE chengji SET name='%s',cno='%d',kaoshi_time='%s',times='%d',scores='%.1f' WHERE Sno='%d"%(a,b,c,d,e,f)
		else:
			exit()

		try:
			cursor.execute(sql)
			db.commit()
		except:
			print('更改失败,没有该学员')
			db.rollback()
		db.close()
		print('更改成功')

	# def d():
	# 	import pymysql
	# 	db = pymysql.connect('localhost','root','asdasd','jiaxiao',charset='utf8')
	# 	cursor = db.cursor()
	# 	print('请问你想修改什么内容')
	# 	q = str(input('修改学员名字:1\n修改学员驾驶证号:2\n修改学员领证时间:3\n修改学员驾驶证领取人:4\n修改学员备注:5\n修改全部:6\n您想修改：'))
	# 	if q == '1':
	# 		a = input('修改的学员名字：')
	# 		b = int(input('修改的学员编号：'))
	# 		sql = "UPDATE lingzheng SET name='%s' WHERE sno='%d' "%(a,b)
	# 	elif q == '2':	
	# 		a = input('修改的学员驾驶证号：')
	# 		b = int(input('修改的学员编号：'))
	# 		sql = "UPDATE lingzheng SET lno='%s' WHERE sno='%d' "%(a,b)
	# 	elif q == '3':	
	# 		a = int(input('修改的学员领证时间：'))
	# 		b = int(input('修改的学员编号：'))
	# 		sql = "UPDATE lingzheng SET receive_time='%s' WHERE sno='%d' "%(a,b)
	# 	elif q == '4':	
	# 		a = input('修改的学员驾驶证领取人：')
	# 		b = int(input('修改的学员编号：'))
	# 		sql = "UPDATE lingzheng SET receive_name='%s' WHERE sno='%d' "%(a,b)
	# 	elif q == '5':	
	# 		a = input('修改的学员备注：')
	# 		b = int(input('修改的学员编号：'))
	# 		sql = "UPDATE lingzheng SET l_text='%s' WHERE sno='%d' "%(a,b)
	# 	elif q == '6':	
	# 		a = input('修改的学员姓名：')
	# 		b = float(input('修改的学员驾驶证号：'))
	# 		c = float(input('修改的学员领证时间：'))
	# 		d = input('修改的学员驾驶证领取人：')
	# 		e = float(input('修改的学员备注：'))
	# 		f = int(input('想要修改的学员编号：'))
	# 		sql = "UPDATE lingzheng SET name='%s',lno='%s',receive_time='%s',receive_name='%s',l_text='%s' WHERE sno='%d"%(a,b,c,d,e,f)
	# 	else:
	# 		exit()

	# 	try:
	# 		cursor.execute(sql)
	# 		db.commit()
	# 	except:
	# 		print('报错')
	# 		db.rollback()
	# 	db.close()
	# 	print('更改成功')



