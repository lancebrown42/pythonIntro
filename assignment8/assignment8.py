class Student:
	intStudentCount = int(0)
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

##########################################################
# Main 
##########################################################
# student1 = Student(str(input("Enter a first name: ")), input("Enter last name: "), input("Enter Gender: "), float(input("Enter GPA: ")), int(input("Enter age: ")))
arrStudents = []
while len(arrStudents) < 2:
	strFirstName = input("Enter a first name: ")
	strLastName = input("Enter last name: ")
	strGender = input("Enter Gender: ")
	dblGPA = float(input("Enter GPA: "))
	intAge = int(input("Enter age: "))
	arrStudents.append(Student(strFirstName, strLastName, strGender, dblGPA, intAge))
Student.displayCount()
print("Male students: %d" % arrStudents.count("Male"))