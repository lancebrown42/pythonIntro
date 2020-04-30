class Customer():
	"""Class defining customer objects"""
	def __init__(self, firstName, lastName, SSN):
		
		self.firstName = firstName
		self.lastName = lastName
		self.SSN = SSN
	@property
	def firstName(self):
		return self._firstName
	@property
	def lastName(self):
		return self._lastName
	@property
	def SSN(self):
		return self._SSN
	@firstName.setter
	def setFirstName(self, val):
		self._firstName = val
	@lastName.setter
	def setLastName(self, val):
		self._lastName = val
	@SSN.setter
	def setSSN(self, val):
		self._SSN = val
	@firstName.getter
	def getFirstName(self):
		return self._firstName
	@lastName.getter
	def getLastName(self):
		return self._lastName
	@SSN.getter
	def getSSN(self):
		return self._lastName
	def addAccount(self):
		#i don't know yet
		return
class Account():
	#Class defining account objects

	#takes customer first name, last name, social and optional starting balance
	def __init__(self, firstName, lastName, SSN, balance=0):
		"""constructor to instantiate account object"""
		
		self.firstName = firstName
		self.lastName = lastName
		self.SSN = SSN
		self.balance = balance
		

	@property
	def firstName(self):
		return self._firstName
	
	@property
	def lastName(self):
		return self._lastName
	
	@property
	def SSN(self):
		return self._SSN
	
	@property
	def accounts(self):
		return self._accounts
	
	@firstName.setter
	def firstName(self, firstName):
		self._firstName = firstName
	
	@lastName.setter
	def lastName(self, lastName):
		self._lastName = lastName
	
	@SSN.setter
	def SSN(self, SSN):
		#validate input
		if len(SSN) != 9:
			raise ValueError("Social security number must be in XXXXXXXXX format")
		else:
			self._SSN = SSN

	@property
	def balance(self):
		return self._balance

	@balance.setter
	def balance(self, amt):
		self._balance = amt

	@balance.getter
	def checkBalance(self):
		return(self._balance)

	def withdraw(self, amt):
		if self.validateMoney(amt):
			self._balance-=amt

	def deposit(self, amt):
		if self.validateMoney(amt):
			self._balance+=amt

	def validateMoney(self, amt):
		#validate monetary values are numeric and positive
		try:
			float(amt)
		except ValueError:
			raise "Value must be numeric"
			return False
		if amt < 0:
			raise ValueError("Value must be positive")
			return False
		else: return True


	def transfer(self, target, amt):
		#transfer funds between accounts
		#usage:
		#	origin.transfer(destination, amount)
		if self.validateMoney(amt):
			self.withdraw(amt)
			target.deposit(amt)

class Savings(Account):
	"""defines savings account object"""
	#inherits Account class, polymorphing deposit, withdraw and instantiation to handle account minimums
	def __init__(self, firstName, lastName, SSN, balance = 0):
		"""constructor to instantiate savings account object"""
		if balance < 500:
			raise Exception("Minimum deposit is $500")
			print("Account not opened")
			return
		else:
			self.balance = balance
			"""inherit Account class init"""
		super().__init__(firstName, lastName, SSN, balance)


	def __str__(self):
		return(("{} {}'s savings account").format(self._firstName, self._lastName))


	def deposit(self, amt):
		if self.validateMoney(amt):
			if amt < 500:
				raise Exception("Minimum deposit is $500")
				return
			else:
				self._balance += amt


	def withdraw(self, amt):
		if self.validateMoney(amt):
			if self._balance - amt < 500:
				raise Exception("Savings cannot be less than $500")
				return
			else:
				self._balance-=amt


class Checking(Account):
	"""constructor to instantiate checking account object"""
	#inherits account class, polymorphing withdraw method to handle overdraft fees
	def __init__(self, firstName, lastName, SSN, balance = 0):
		super().__init__(firstName, lastName, SSN, balance)
		
	
	def __str__(self):
		return(("{} {}'s checking account").format(self._firstName, self._lastName))
	
	def withdraw(self, amt):
		if self.validateMoney(amt):
			if self._balance - amt < 0:
				self._balance -= (amt + 20)
			else:
				self._balance -= amt


		


##Main


#instantiate
savings1 = Savings("John", "Doe", "123456789", 1200)
checking1 = Checking("John", "Doe", "123456789", 500)

#display
print(savings1)
print(checking1)

#check balance
print(savings1.checkBalance)
print(checking1.checkBalance)

#transfer
savings1.transfer(checking1, 100)
print(savings1.checkBalance)
print(checking1.checkBalance)
checking1.transfer(savings1, 600)
print(savings1.checkBalance)
print(checking1.checkBalance)
