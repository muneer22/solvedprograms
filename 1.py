#class Test:

#	def fun(self):
#		print("Hello")

#obj = Test()
#obj.fun()

class Person:

	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Hello, my name is', self.name)

p = Person('Muneer')
p.say_hi()

