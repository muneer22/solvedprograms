class CSStudent(object):
	stream = 'CSE'

	def __init__(self, name, roll_no, reg_no):
		self.name = name
		self.roll_no = roll_no
		self.reg_no = reg_no

#Objects of class
a = CSStudent("Muneer", "22", "IUST/BTECH/13/1330")
b = CSStudent("xxxxxx", "01", "IUST/BTECH/13/1440")
c = CSStudent("YYYYYY", "02", "IUST/BTECH/13/1520")


print("Name", "Roll_no", "Reg_no", "Stream")
print(a.name, a.roll_no, a.reg_no, a.stream)
print(b.name, b.roll_no, b.reg_no, b.stream)
print(c.name, c.roll_no, c.reg_no, c.stream)
