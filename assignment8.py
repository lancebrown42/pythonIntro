class Student:
	intStudentCount = int(0)
	def __init__(self, strFirstName, strLastName, strGender, dblGPA, intAge):
		self.strFirstName = strFirstName
		self.strLastName = strLastName
		self.strGender = strGender
		self.dblGPA = dblGPA
		self.intAge = intAge
		intStudentCount += 1
	def displayStudent(self):
		print("Name: %s %s, Gender: %s, GPA: %0.1f, Age: %d" % (strFirstName, strLastName, strGender, dblGPA, intAge))
	def displayCount(self):
		print("Total number of students: %d" % Student.intStudentCount)

##########################################################
# Main 
##########################################################
student1 = Student(str(input("Enter a first name: ")), input("Enter last name: "), input("Enter Gender: "), float(input("Enter GPA: ")), int(input("Enter age: ")))
# arrStudents = []
# for i in range(4):
# 	arrStudents.append(Student(input("Enter a first name: "), input("Enter last name: "), input("Enter Gender: "), float(input("Enter GPA: ")), int(input("Enter age: "))))
# Student.displayCount()
# print("Male students: %d" % arrStudents.count("Male"))