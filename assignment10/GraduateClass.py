##########################################
#Assignment 10
#Lance Brown
# 3/31/20
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
    @property
    def gradYear(self):
        return self._gradYear
    @property
    def jobStatus(self):
        return self._jobStatus

    @gradYear.setter
    def gradYear(self, gradYear):
        if gradYear < 1800:
            raise Exception("The school wasn't founded until 1800, provide a valid grad date")
        elif gradYear > 2020:
            raise Exception("Time travel is unlikely. Provide a grad date in the past")
        else:
            try:
                self._gradYear = int(gradYear)
            except TypeError as e:
                raise e("Enter an integer year")
    @jobStatus.setter
    def jobStatus(self, jobStatus):
        if jobStatus != 'Y' and jobStatus != 'N':
            raise Exception("jobStatus can only be 'Y' or 'N'")
        else:
            self._jobStatus = jobStatus
    
    def __str__(self):
        return("Total graduates: {}").format(self.gradCount)
    def displayTotal():
        print("Number of males: %d \nNumber of females: %d" % (Student.intMaleCount, Student.intFemaleCount))