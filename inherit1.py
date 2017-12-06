class Person(object):
#Constructor
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	def isEmployee(self):
		return False


# Inherited or sub class from Person class
class Employee(Person):

	def isEmployee(self):
		return True

	def isIntern(self):
		return ("Intern")


emp = Person("Muneer")
print(emp.getName(), emp.isEmployee())

emp = Employee("Faizan")
print(emp.getName(), emp.isEmployee(), emp.isIntern())


# Shows is a class subclass or not.
print(issubclass(Employee, Person))
print(issubclass(Person, Employee))
