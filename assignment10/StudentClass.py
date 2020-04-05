##########################################
#Assignment 10
#Lance Brown
# 3/31/20
#########################################
from PersonClass import Person as Person
class Student(Person):
    #'Subclass for all students, inherits person
   
    stuStudentCount = 0
    stuMaleCount = 0
    stuFemaleCount = 0
    stuGPATotal = 0 
    stuFemaleAgeTotal = 0
    stuMaleAgeTotal = 0 
   
      
    def __init__(self, firstname, lastname, gender, age, GPA):
      super().__init__(firstname, lastname, gender, age)
      Student.stuStudentCount += 1
      if (gender == 'Male'):
        Student.stuMaleCount += 1
        Student.stuMaleAgeTotal += age
      else:
        Student.stuFemaleCount += 1
        Student.stuFemaleAgeTotal += age
      Student.stuGPATotal += GPA
    @property
    def GPA(self):
      return self._GPA
    @GPA.setter
    def GPA(self, GPA):
      if GPA > 4:
        raise Exception("GPA out of range, must be less than 4.0")
      elif GPA < 1:
        raise Exception("GPA out of range, must be positive")
      else:
        try:
          self._GPA = float(GPA)
        except Exception as e:
          raise e
        

    
    
    
    def displayTotal(self):
        print("Number of males: %d \nNumber of females: %d" % (Student.intMaleCount, Student.intFemaleCount))