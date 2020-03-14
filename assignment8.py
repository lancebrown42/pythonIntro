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
	def displayStudent(self):
		print("Name: %s %s, Gender: %s, GPA: %0.1f, Age: %d" % (strFirstName, strLastName, strGender, dblGPA, intAge))
	def displayCount():
		print("Total number of students: %d" % Student.intStudentCount)


def validateGender(strGender):
	if strGender != "MALE" and strGender != "FEMALE" and strGender != "M" and strGender != "F":
		validateGender((input("Please enter 'male' or 'female': ")).upper())
	else:
		return strGender[0]

##########################################################
# Main 
##########################################################
# student1 = Student(str(input("Enter a first name: ")), input("Enter last name: "), input("Enter Gender: "), float(input("Enter GPA: ")), int(input("Enter age: ")))
arrStudents = []
while len(arrStudents) < 2:
	strFirstName = input("Enter a first name: ")
	strLastName = input("Enter last name: ")
	strGender = validateGender((input("Enter Gender: ")).upper())
	dblGPA = float(input("Enter GPA: "))
	intAge = int(input("Enter age: "))
	arrStudents.append(Student(strFirstName, strLastName, strGender, dblGPA, intAge))
Student.displayCount()
print(arrStudents[0])
print("Male students: %d" % arrStudents.count("M"))
print("Female students: %d" % arrStudents.count("F"))