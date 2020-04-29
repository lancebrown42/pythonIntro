
class Customer():
	"""Class defining customer objs"""
	
	def __init__(self, firstName, lastName, SSN):
            """constructor to instantiate customer object"""
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
		self._SSN = SSN
        #overrides string function to return useful data
	def __str__(self):
		return self._firstName + " " + self._lastName + " " + self._SSN

class Account(Customer):
	#Class defining account objs
	def __init__(self, firstName, lastName, SSN, balance=0):
        """constructor to instantiate account object"""
        """inherit the Customer init"""
		super(Account, self).__init__(firstName, lastName, SSN)
		if balance != 0:
			self.balace = balance

	@property
	def balance(self):
		return self._balance
	@balance.setter
	def balance(self, amt):
		self._balance = amt
	def checkBalance(self):
		print(str(self.__name__) + ": $" + str(self._balance))
	def withdraw(self, amt):
		if self.validateMoney(amt):
			self._balance-=amt
	def deposit(self, amt):
		if self.validateMoney(amt):
			self._balance+=amt
	def validateMoney(self, amt):
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
	"""defines savings"""
	def __init__(self, firstName, lastName, SSN, balance = 0):
            """constructor to instantiate savings account object"""
		if balance < 500:
			raise Exception("Minimum deposit is $500")
			print("Account not opened")
			return
		else:
			self.balance = balance
		    """inherit Account class init"""
		super(Savings, self).__init__(firstName, lastName, SSN, balance)
	def __str__(self):
		return(("{} {}'s savings account").format(self._firstName, self._lastName))
	def deposit(self, amt):
		if self.validateMoney(amt):
			if amt < 500:
				raise Exception("Minimum deposit is $500")
				return
			else:
				self._balance += amt
class Checking(Account):
	def __init__(self, firstName, lastName, SSN, balance = 0):
		super(Checking, self).__init__(firstName, lastName, SSN, balance)
		self.balance = balance
	def __str__(self):
		return(("{} {}'s checking account").format(self._firstName, self._lastName))
	def withdraw(self, amt):
		if self.validateMoney(amt):
			if self._balance - amt < 0:
				self._balance -= amt + 20
			else:
				self._balance -= amt


		

##Main
john = Customer("John", "Doe", "123456789")
print(john)
savings1 = Savings("John", "Doe", "123456789", 600)
checking1 = Checking("John", "Doe", "123456789", 600)
print(savings1)
print(checking1)
savings1.checkBalance()
checking1.checkBalance()
savings1.transfer(checking1, 200)
savings1.checkBalance()
checking1.checkBalance()