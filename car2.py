from abc import ABC, ABCMeta, abstractmethod

class Vehicle(ABC):


	#__metaclass__ = ABCMeta


	base_sale_price = 0
	wheels = 0

	def __init__(self, miles, make, model, year, sold_on):

		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on


	def sale_price(self):
		if self.sold_on is not None:
			return 0.0
		return 5000.0 * self.wheels


	def purchase_price(self):
		if self.sold_on is None:
			return 0.0
		return 8000 - (.10 * self.miles)

	@abstractmethod
	def vehicle_type():
		pass 
 # if we have to override this @abstractmethod we don't have to pass ABC to Vehicle instead pass object.
 # & uncomment __metaclass__.
 

class car(Vehicle):

	base_sale_price = 8000
	wheels = 4

	def vehicle_type(self):

		return 'car'


class Truck(Vehicle):

	base_sale_price = 10000
	wheels = 4

	def vehicle_type(self):
		return 'truck'

class Motorcycle(Vehicle):

	base_sale_price = 4000
	wheels = 2

	def vehicle_type(self):
		return 'motorcycle'


n = Vehicle(20, 'Maruti Suzuki', 'Van', 2000, 2017)
print(n.purchase_price())

v = car(36, 'Honda', 'Accord', 2014, 2017)

print (v.purchase_price())
#print(v.sale_price())

t = Truck(50, 'TATA', 'Tipper', 2012, None)

print(t.purchase_price())
print(t.sale_price())
print (t.base_sale_price)

m = Motorcycle(50000, 'Pulsar', 'NS-200', 2010, 2017)

print (m.purchase_price())
print(m.sale_price())
print(m.model)



