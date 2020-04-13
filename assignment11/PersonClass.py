##########################################
#Assignment 11
#Lance Brown
# 4/13/20
#########################################
class Person:
	#Common class for all people
	def __init__(self, firstname, lastname, gender, age):
		self._firstname = firstname
		self._lastname = lastname
		self._gender = gender
		self._age = age
	@property
	def firstname(self):
		return self._firstname
	@property
	def lastname(self):
		return self._lastname
	@property
	def gender(self):
		return self._gender
	@property
	def age(self):
		return self._age
	
	@firstname.setter
	def firstname(self, firstname):
		if len(self.firstname) < 1:
			raise Exception("First name cannot be empty")
		else:
			self.firstname = firstname
	@lastname.setter
	def lastname(self, lastname):
		if len(lastname) < 1:
			raise Exception("Last name cannot be empty")
		else:
			self._lastname = lastname
	@gender.setter
	def setGender(self, gender):
		if gender != 'Male' and gender != 'Female':
			raise Exception("Gender can be 'Male' or 'Female'")
		else:
			self._gender = gender
	@age.setter
	def age(self, age):
		try:
			self._age = int(age)
		except TypeError:
			raise TypeError("Age must be in integer format")
		if age < 0:
			raise Exception("Age must be a positive number")
		elif age > 200:
			raise Exception("That age is very unrealistic")
	def schoolStatus(self):
		print("Undefined")

