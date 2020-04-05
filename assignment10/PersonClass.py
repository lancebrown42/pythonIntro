##########################################
#Assignment 9
#Lance Brown
# 3/21/20
#########################################
class Person:
    #Common class for all people
    def __init__(self, firstname, lastname, gender, age):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
   	def setFirstName(self, firstname):
   		if len(firstname) < 1:
   			raise Exception("First name cannot be empty")
		self.firstname = firstname
	def setLastName(self, lastname):
		if len(lastname) < 1:
			raise Exception("Last name cannot be empty")
		self.lastname = lastname
	def setGender(self, gender):
		try:
			gender = upper(gender)[slice(1)]
			print(gender)
		except:
			raise("gender error")