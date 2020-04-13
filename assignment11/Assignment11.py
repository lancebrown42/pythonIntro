##########################################
#Assignment 11
#Lance Brown
# 4/13/20
#########################################
from PersonClass import Person as Person
from StudentClass import Student as Student
from GraduateClass import Graduate as Graduate




##########################################################
# Main 
##########################################################

#This would create first object from the Student class"
Graduate1 = Graduate("Bill", "Zara", "Male", 20, 3.25, 2019, "Y")

#"This would create second object from the Student class"
Graduate2 = Graduate("Betty", "Tara", "Female", 25, 2.25, 2018, "N")

#"This would create third object from the Student class"
Graduate3 = Graduate("Sydney", "Nye", "Female", 30, 3.75, 2018, "Y")

#"This would create forth object from the Student class"
Graduate4 = Graduate("Jake", "Leedom", "Male", 35, 2.75, 2017, "N")

#"This would create fifth object from the Student class"
Graduate5 = Graduate("Alex", "Jacobs", "Male", 21, 3.55, 2010, "Y")

Student1 = Student("Jim", "Beam", "M", 21, 4.0)


print (Graduate5)
print (Student1)
Graduate.schoolStatus(Graduate1)
Student.schoolStatus(Graduate1)
Person.schoolStatus(Graduate1)
print ("Average GPA of all Students is  ", Student.stuGPATotal/Student.stuStudentCount)
print ("Average Age of Male Students is  ", Student.stuMaleAgeTotal/Student.stuMaleCount)
print ("Average Age of Female Students is  ", Student.stuFemaleAgeTotal/Student.stuFemaleCount)
print ("Number of employed male students is ", Graduate.gradEmployedMaleCount)
print ("Number of employed female students is ", Graduate.gradEmployedFemaleCount)