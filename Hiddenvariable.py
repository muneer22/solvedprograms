class MyClass:

	__hiddenVariable = 0

	def add(self, increment):
		self.__hiddenVariable += increment
		print(self.__hiddenVariable)



obj = MyClass()
# In order to retrive hidden variable we can use _, __ other wise error will be there.
print(obj._MyClass__hiddenVariable)

obj.add(5)
obj.add(5)

#print (obj.__hiddenVariable)

print(obj._MyClass__hiddenVariable)