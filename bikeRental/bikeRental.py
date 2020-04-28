##########################################
#Bike rental
#Lance Brown
# 4/20/20
#########################################
class Customer():
	def __init__(self, firstName, lastName, rentalType):
		self._firstName = firstName
		self._lastName = lastName
		self._rentalType = rentalType
	@property
	def rentalType(self):
		return self._rentalType
	@property
	def firstName(self):
		return self._firstName
	@property
	def lastName(self):
		return self._lastName
	@rentalType.setter
	def rentalType(self, rentType):
		self._rentalType = rentType
	
	def viewBikes(self, shop):
		return shop.checkInventory
	def requestBikes(self, quantity, shop):
		if quantity <= shop.checkInventory:
			print(("You may rent {} bikes").format(quantity))
		else:
			print("Insufficient bikes onhand.")
	def changeRentalType(self, newType):
		self.rentalType = newType
class Shop():

	def __init__(self, inventory):
		self._inventory = inventory
		self._rentalCost = {
		"hour" : float(5),
		"day" : float(20),
		"week" : float(60)
		}
	@property
	def inventory(self):
		return self._inventory
	@property
	def rentalCost(self):
		return self._rentalCost
	@inventory.getter
	def checkInventory(self):
		return self._inventory
	@inventory.setter
	def inventory(self, value):
		self._inventory = value
	def rentBike(self, quantity):
		self.inventory -= quantity
		print(("{} bikes checked out, {} remaining").format(quantity, self.inventory))
	def returnBike(self, quantity):
		self.inventory += quantity
		print(("{} bikes returned, {} remaining").format(quantity, self.inventory))
	def billCustomer(self, quantity, customer, duration):
		discount = 1
		if quantity >= 3 and quantity <= 5:
			discount = 0.7
		total = self.rentalCost.get(customer.rentalType) * duration * quantity * discount
		print(("${:.2f} due for rental of {:d} bikes for {:d} {}s").format(total, quantity, duration, customer.rentalType))

	
	
##########################################################
# Main 
##########################################################
John = Customer("John", "Doe", "hour")
Shop = Shop(20)
print(John.viewBikes(Shop))
John.requestBikes(15, Shop)
John.requestBikes(21, Shop)
Shop.rentBike(15)
Shop.returnBike(15)
Shop.billCustomer(15, John, 3)
John.changeRentalType("day")
Shop.billCustomer(3, John, 2)