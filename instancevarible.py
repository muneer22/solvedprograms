class CSStudent:

	stream = 'CSE'

	def __init__(self, roll):
		self.roll = roll


	def setAddress(self, address):
		self.address = address


	def getAddress(self):
		return self.address


a = CSStudent(22)
print(a.stream)
a.setAddress("Zakura,J&K")
print(a.roll)
print(a.getAddress())
# Changing class members.
a.stream = 'ECE'
print(a.stream)
