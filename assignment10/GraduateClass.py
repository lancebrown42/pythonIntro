##########################################
#Assignment 9
#Lance Brown
# 3/21/20
#########################################
from StudentClass import Student as Student
class Graduate(Student):
    #Subclass for graduates, inherits student
    gradCount = 0
    gradEmployedMaleCount = 0
    gradEmployedFemaleCount = 0

    def __init__(self, firstname, lastname, gender, age, GPA, gradYear, jobStatus):
        super().__init__(firstname, lastname, gender, age, GPA)
        Graduate.gradCount += 1
        self.gradYear = gradYear
        self.jobStatus = jobStatus
        if gender == 'Male' and jobStatus == 'Y':
            Graduate.gradEmployedMaleCount += 1
        elif gender == 'Female' and jobStatus == 'Y':
            Graduate.gradEmployedFemaleCount += 1
    def __str__(self):
        return("Total graduates: {}").format(self.gradCount)
    def displayTotal():
        print("Number of males: %d \nNumber of females: %d" % (Student.intMaleCount, Student.intFemaleCount))