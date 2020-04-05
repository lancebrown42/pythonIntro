##########################################################
# Lance Brown
# Assignment 8
##########################################################
class Student:
	intStudentCount = int(0)
	intMaleCount = int(0)
	intFemaleCount = int(0)
	intMaleAgeTotal = int(0)
	intFemaleAgeTotal = int(0)
	intGPATotal = float(0)
	def __init__(self, strFirstName, strLastName, strGender, dblGPA, intAge):
		self.strFirstName = str(strFirstName)
		self.strLastName = str(strLastName)
		self.strGender = str(strGender)
		self.dblGPA = float(dblGPA)
		self.intAge = int(intAge)
		Student.intStudentCount += 1
		if strGender == "M":
			Student.intMaleCount += 1
			Student.intMaleAgeTotal += self.intAge
		elif strGender == "F":
			Student.intFemaleCount += 1
			Student.intFemaleAgeTotal += self.intAge
		Student.intGPATotal += self.dblGPA
##########################################################
#  Display count- displays total number of students
##########################################################
	def displayCount():
		print("Total number of students: %d" % Student.intStudentCount)
##########################################################
# Display Genders- displays number of male and female students
##########################################################
	def displayGenders():
		print("Number of males: %d \nNumber of females: %d" % (Student.intMaleCount, Student.intFemaleCount))
##########################################################
# Display Average GPA- displays average gpa
##########################################################
	def displayAverageGPA():
		print("Average GPA: %0.1f" % (Student.intGPATotal/Student.intStudentCount))
##########################################################
# Display average age- displays average age
##########################################################
	def displayAverageAge():
		print("Average age of males: %d\nAverage age of females: %d" % (Student.intMaleAgeTotal/Student.intMaleCount, Student.intFemaleAgeTotal/Student.intFemaleCount))
