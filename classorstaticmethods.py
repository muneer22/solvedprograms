from datetime import date

class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age


	# A class method to create a person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# A static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person("MUNEER", "24")
person2 = Person.fromBirthYear("MUNEER", 1993)

print (person1.age)
print(person2.age)

# print the result
print (Person.isAdult(17))
print (Person.isAdult(18))
print (Person.isAdult(19))

