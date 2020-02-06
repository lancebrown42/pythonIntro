#--------------------------------------------------
# Lance Brown
# Assignment 4
#--------------------------------------------------


#-----------------------------------------------------
# Problem 1 - Print the largest of four numbers
#-------------------------------------------------------
# print("Please enter 4 whole numbers: ")
# arrNumbers = list()
# for i in range(4):
	# intNumber = input("Number " + str(i + 1) + ": ")
	# arrNumbers.append(int(intNumber))
# arrNumbers.sort(reverse = True)
# print(str(arrNumbers[0]) + " is the largest number provided.")
#------------------------------------------------------------------
#Problem 2 - Determine if a year is a leap year
#----------------------------------------------------------------------

intYear = int(input("Enter a year: "))
if intYear <= 1500 or intYear >= 2200:
	print("Invalid Year")
elif intYear % 100 == 0:
	if intYear % 400 == 0:
		print("Yes, " + str(intYear) + " is a leap year.")
	else:
		print("No, " + str(intYear) + " is not a leap year.")
elif intYear % 4 == 0:
	print("Yes, " + str(intYear) + " is a leap year.")
else:
	print("No, " + str(intYear) + " is not a leap year.")
	
