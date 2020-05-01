#################################################
#Lance Brown
#Final Project
#4/25/20
#################################################

class Account():
	"""Class defining account objects"""


	_customers = {} #class dict to store accounts by customer ssn
	#takes customer first name, last name, social and optional starting balance
	def __init__(self, firstName, lastName, SSN, balance=0):
		"""constructor to instantiate account object"""

		
		self.setFirstName = firstName
		self.setLastName = lastName
		self.setSSN = SSN
		self.setBalance = balance
		#initialize customer in dict if new, or update if existing
		Account._customers.setdefault(SSN,[]).append(self)
	
	#Account props	
	##################################
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
	
	@property
	def balance(self):
		return self._balance

	#setters
	################################

	@firstName.setter
	def setFirstName(self, firstName):
		self._firstName = firstName
	
	@lastName.setter
	def setLastName(self, lastName):
		self._lastName = lastName
	
	@SSN.setter
	def setSSN(self, SSN):
		#validate input
		if len(SSN) != 9:
			raise ValueError("Social security number must be in XXXXXXXXX format")
		else:
			self._SSN = SSN

	@balance.setter
	def setBalance(self, amt):
		self._balance = amt

	#getters
	#############################
	@firstName.getter
	def getFirstName(self):
		return self._firstName

	@lastName.getter
	def getLastName(self):
		return self._lastName

	@SSN.getter
	def getSSN(self):
		return self._SSN

	@balance.getter
	def checkBalance(self):
		return(self._balance)

	#methods
	#############################

	#deduct funds from account
	def withdraw(self, amt):
		if self.validateMoney(amt):
			self.setBalance-=amt

	#add funds to account
	def deposit(self, amt):
		if self.validateMoney(amt):
			self.setBalance+=amt

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
		#   origin.transfer(destination, amount)
		if self.validateMoney(amt) and self.validateMoney(self.checkBalance - amt):
			self.withdraw(amt)
			target.deposit(amt)
		
	
	#get the total balance for all accounts for a specified customer
	def totalBalance(SSN):
		total = 0
		#get a list of all accounts specified customer has
		accounts = Account._customers.get(SSN)
		for account in accounts:
			total += float(account.checkBalance)
		return total

	#override str to something almost meaningful
	def __str__(self):
		return(("{} {}'s {} account").format(self.getFirstName, self.getLastName, self.__class__.__name__))


class Savings(Account):
	"""defines savings account object
	inherits Account class, polymorphing deposit, withdraw and instantiation to handle account minimums"""
	def __init__(self, firstName, lastName, SSN, balance = 0):
		"""constructor to instantiate savings account object"""
		if balance < 500:
			raise Exception("Minimum deposit is $500")
			print("Account not opened")
			return
		else:
			self.setBalance = balance
			"""inherit Account class init"""
		super().__init__(firstName, lastName, SSN, balance)



	#add funds
	def deposit(self, amt):
		if self.validateMoney(amt):
			#check if deposit is above minimum
			if amt < 500:
				raise Exception("Minimum deposit is $500")
				return
			else:
				self.setBalance += amt


	def withdraw(self, amt):
		if self.validateMoney(amt):
			if self.setBalance - amt < 500:
				raise Exception("Savings cannot be less than $500")
				return
			else:
				self.setBalance-=amt


class Checking(Account):
	"""constructor to instantiate checking account object
	inherits account class, polymorphing withdraw method to handle overdraft fees"""
	def __init__(self, firstName, lastName, SSN, balance = 0):
		super().__init__(firstName, lastName, SSN, balance)
		
	
	#deduct funds
	def withdraw(self, amt):
		if self.validateMoney(amt):
			#if withdrawal results in negative value apply 20 overdraft fee
			if self.setBalance - amt < 0:
				self.setBalance -= (amt + 20)
			else:
				self.setBalance -= amt


		

#################################################
##Main
#################################################

#instantiate
Customer1 = ("John", "Doe", "123456789")
Customer2 = ("Jane", "Eyre", "781239812")
savings1 = Savings(Customer1[0], Customer1[1], Customer1[2], 1000)
savings2 = Savings(Customer1[0], Customer1[1], Customer1[2], 13000)
checking1 = Checking(Customer1[0], Customer1[1], Customer1[2], 1000)
checking2 = Checking(Customer2[0], Customer2[1], Customer2[2])

#display __str__
print(savings1)
print(checking2)

#check balance
print("savings1 balance: " + str(savings1.checkBalance))
print("checking1 balance: " + str(checking1.checkBalance))
print("savings2 balance: " + str(savings2.checkBalance))
print("checking2 balance: " + str(checking2.checkBalance))


#deposit
savings1.deposit(600) #change to <500 to get an error
checking2.deposit(100)
print("Deposit 600 to savings1 and 100 to checking2")
print("savings1 " + str(savings1.checkBalance))
print("checking2 " + str(checking2.checkBalance))
#withdraw
print("withdraw 3000 from savings2 and 100 from checking1")
savings2.withdraw(3000)
checking1.withdraw(100)
print("savings2 " + str(savings2.checkBalance))
print("checking1 " + str(checking1.checkBalance))
#transfer
savings1.transfer(checking1, 100)
print("Transfer 100 from savings1 to checking1")
print("savings1 " + str(savings1.checkBalance))
print("checking1 " + str(checking1.checkBalance))
checking1.transfer(savings1, 600)
print("Transfer 600 from checking1 to savings1")
print("savings1 " + str(savings1.checkBalance))
print("checking1 " + str(checking1.checkBalance))
#total balance
print("totalBalance Customer1 " + str(Account.totalBalance(Customer1[2])))
