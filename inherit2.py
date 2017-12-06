class Man:

	def __init__(self):
		self.str1 = "Human"
		print ("Man")

class Women:

	def __init__(self):
		self.str2 = "Human"
		print ("Women")

class Animal(Man, Women):

	def __init__(self):

		#Calling consturctor of base classes.
		Man.__init__(self)
		Women.__init__(self)
		print ("Animal")

	def printStrs(self):
		print(self.str1, self.str2)

ob = Animal()
ob.printStrs()