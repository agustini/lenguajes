a = 8
def fun1():
	def fun2():
		def fun3():
			global a
			print a
		a=12
		fun3();
		print a
	a = 6
	fun2()
	print a
	return a
fun1()
print a
raw_input("presione algo para salir") 
