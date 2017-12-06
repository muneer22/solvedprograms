class CSStudent:

	stream = 'CSE'

	def __init__(self, roll):
		self.roll = roll

a = CSStudent(22)
b = CSStudent(23)

print(a.stream)
print(b.stream)
print(a.roll)
print(b.roll)

print(CSStudent.stream)