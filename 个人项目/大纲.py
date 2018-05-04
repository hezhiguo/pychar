from 学籍信息 import TJ
from 学生信息删除 import SC
from 学生信息查询 import CZ
from 学生信息修改 import XG
print('开始')
class q(object):
	def start():
		print('欢迎来到天意学校\n请问你有什么想做的么\n登录请输:1  注册请输:2  查看请输:3')
		a = str(input('您现在想：'))
		if a == '1':
			import 登录
			q.all()
		elif a == '2':
			print('')
			import 管理员信息
			print('\n登录请输:1  退出请输:2')
			o = str(input('您的选择：'))
			if o == '1':
				import 登录
				q.all()
			elif o == '2':
				exit()
			else:
				print('对不起,输入错误')
		elif a == '3':
			print('您现在进入了查询模式\n')
			q.a()
		else:
			print('对不起，对于不听劝告的人，我们一般采取区别对待，再见。')
			exit()

	def a():#查看模块
		print('*' * 30)
		print('请问您想查看什么')
		print('1、查看学生基本信息\n2、查看学生体检信息\n3、查看学生成绩\n4、返回上一级\n5、退出查询\n')
		z = str(input('请输入您的选择：'))
		if z == '1':
			print('*' * 30)
			CZ.a()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.a()
		elif z == '2':
			print('*' * 30)
			CZ.b()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.a()
		elif z == '3':
			print('*' * 30)
			CZ.c()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.a()
		# elif z == '4':
		# 	print('*' * 30)
		# 	CZ.d()
		# 	a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
		# 	if a == '1':
		# 		q.b()
		# 	elif a == '2':
		# 		q.all()
		# 	else:
		# 		print('输入错误,再见')
		# 		exit()
		# 	q.a()
		elif z == '4':
			print('')
			print('*' * 30)
			q.all()
		elif z == '5':
			exit()
		else:
			print('对不起，输入错误，请重新输入\n')
			q.a()

	def b(): #增加模块
		print('*' * 30)
		print('1、添加学生基本信息\n2、添加学生体检信息\n3、添加学生成绩\n4、返回上一级\n5、退出查询\n')
		z = str(input('请输入您的选择：'))
		if z == '1':
			print('*' * 30)
			TJ.a()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
		elif z == '2':
			print('*' * 30)
			TJ.b()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.all()
		elif z == '3':
			print('*' * 30)
			TJ.c()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.all()
		# elif z == '4':
		# 	print('*' * 30)
		# 	TJ.d()
		# 	a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
		# 	if a == '1':
		# 		q.b()
		# 	elif a == '2':
		# 		q.all()
		# 	else:
		# 		print('输入错误,再见')
		# 		exit()
		# 	q.all()
		elif z == '4':
			print('*' * 30)
			q.all()
		elif z == '5':
			exit()
		else:
			print('对不起，输入错误，请重新输入\n下次错误将强制退出')
			q.b2()

	def b2(): #增加模块
		print('*' * 30)
		print('1、添加学生基本信息\n2、添加学生体检信息\n3、添加学生成绩\n4、返回上一级\n5、退出查询\n')
		z = str(input('请输入您的选择：'))
		if z == '1':
			print('*' * 30)
			import b学籍信息模块备份
			print('\n请问您接下来想干什么？\n 返回来了')
			q.b()
		elif z == '2':
			print('*' * 30)
			import c体检信息模块备份
			print('\n请问您接下来想干什么？\n')
			q.all()
		elif z == '3':
			print('*' * 30)
			import e成绩模块备份
			print('\n请问您接下来想干什么？\n')
			q.all()
		# elif z == '4':
		# 	print('*' * 30)
		# 	import f领证模块备份
		# 	print('\n请问您接下来想干什么？\n')
		# 	q.all()
		elif z == '4':
			print('*' * 30)
			q.all()
		elif z == '5':
			exit()
		else:
			exit()


	def all():
		print('*' * 30)
		w = input('\n请问您想做什么,尊敬的管理员先生\n1、添加学生信息\n2、修改学生信息\n3、删除学生信息\n4、查看学生信息\n5、退出程序\n您的选择是：')
		if w == '1':
			print('您进入了添加模式\n')
			q.b()
		elif w == '2':
			print('您进入了修改模式\n')
			q.x()
		elif w == '3':
			print('您进入了删除模式\n')
			q.s()
		elif w == '4':
			print('您进入了查询模式\n')
			q.a()
		elif w == '5':
			exit()
		else:
			print('输入错误，请重新输入，如果再错，将强制退出\n')
			p.alll()

	def alll():
		print('*' * 30)
		w = input('请问您想做什么,尊敬的管理员先生\n1、添加学员信息\n2、修改学员信息\n3、删除学员信息\n4、查看学员信息\n5、退出程序\n您的选择是：')
		if w == '1':
			print('您进入了添加模式\n')
			q.b()
		elif w == '2':
			print('您进入了修改模式\n')
			q.x()
		elif w == '3':
			print('您进入了删除模式\n')
			q.s()
		elif w == '4':
			print('您进入了查询模式\n')
			q.a()
		elif w == '5':
			exit()
		else:
			exit()

	def x():#修改模块
		print('*' * 30)
		print('请问您想修改什么\n1、修改学生基本信息\n2、修改学生体检信息\n3、修改学生成绩\n4、返回上一级\n')
		z = str(input('请输入您的选择：'))
		if z == '1':
			print('*' * 30)
			XG.a()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.all()
		elif z == '2':
			print('*' * 30)
			XG.b()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.all()
		elif z == '3':
			print('*' * 30)
			XG.c()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.all()
		# elif z == '4':
		# 	print('*' * 30)
		# 	XG.d()
		# 	a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
		# 	if a == '1':
		# 		q.b()
		# 	elif a == '2':
		# 		q.all()
		# 	else:
		# 		print('输入错误,再见')
		# 		exit()
		# 	q.all()
		elif z == '4':
			print('*' * 30)
			q.all()
		elif z == '5':
			exit()

	def s():#删除模块
		print('*' * 30)
		print('请问您想修改什么\n1、删除学生基本信息\n2、删除学生体检信息\n3、删除学生成绩\n4、删除学生领证情况\n5、返回上一级\n')
		z = str(input('请输入您的选择：'))
		if z == '1':
			print('*' * 30)
			SC.a()	
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.all()
		elif z == '2':
			print('*' * 30)
			SC.b()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.all()
		elif z == '3':
			print('*' * 30)
			SC.c()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.all()
		elif z == '4':
			print('*' * 30)
			SC.d()
			a = str(input('\n请问您接下来想干什么？\n留在此处:1  返回上一级:2\n您的选择是：'))
			if a == '1':
				q.b()
			elif a == '2':
				q.all()
			else:
				print('输入错误,再见')
				exit()
			q.all()
		elif z == '5':
			print('*' * 30)
			q.all()
		elif z == '6':
			exit()

q.start()

