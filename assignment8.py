class Student:
	intStudentCount = int(0)
	intMaleCount = int(0)
	intFemaleCount = int(0)
	def __init__(self, strFirstName, strLastName, strGender, dblGPA, intAge):
		self.strFirstName = strFirstName
		self.strLastName = strLastName
		self.strGender = strGender
		self.dblGPA = dblGPA
		self.intAge = intAge
		Student.intStudentCount += 1
		if strGender == "M":
			Student.intMaleCount += 1
		elif strGender == "F":
			Student.intFemaleCount += 1
	def displayStudent(self):
		print("Name: %s %s, Gender: %s, GPA: %0.1f, Age: %d" % (strFirstName, strLastName, strGender, dblGPA, intAge))
	def displayCount():
		print("Total number of students: %d" % Student.intStudentCount)
	def displayGenders():
		print("Number of males: %d \nNumber of females: %d" % (Student.intMaleCount, Student.intFemaleCount))


def validateGender(strGender):
	if strGender != "MALE" and strGender != "FEMALE" and strGender != "M" and strGender != "F":
		validateGender((input("Please enter 'male' or 'female': ")).upper())
	else:
		return strGender[0]
def validateGPA(dblGPA):
	try:
		dblGPA = float(dblGPA)
	except ValueError:
		dblGPA = validateGPA(input("Enter a numerical value: "))
	if dblGPA < 0 or dblGPA > 4:
		dblGPA = validateGPA(input("Enter a valid GPA from 0-4: "))
	else:
		return dblGPA
def validateAge(intAge):
	try:
		intAge = int(intAge)
	except ValueError:
		intAge = validateAge(input("Enter a numerical value: "))
	if intAge <= 0 or intAge > 200:
		intAge = validateAge(input("Enter a valid age: "))
	

##########################################################
# Main 
##########################################################
# student1 = Student(str(input("Enter a first name: ")), input("Enter last name: "), input("Enter Gender: "), float(input("Enter GPA: ")), int(input("Enter age: ")))
arrStudents = []
while len(arrStudents) < 2:
	strFirstName = input("Enter a first name: ")
	strLastName = input("Enter last name: ")
	strGender = validateGender((input("Enter Gender: ")).upper())
	dblGPA = validateGPA(input("Enter GPA: "))
	intAge = validateAge(input("Enter age: "))
	arrStudents.append(Student(strFirstName, strLastName, strGender, dblGPA, intAge))
Student.displayCount()
Student.displayGenders()