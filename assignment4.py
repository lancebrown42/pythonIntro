#--------------------------------------------------
# Lance Brown
# Assignment 4
#--------------------------------------------------


#-----------------------------------------------------
# Problem 1 - Print the largest of four numbers
#-------------------------------------------------------
print("Please enter 4 whole numbers: ")
arrNumbers = list()
for i in range(4):
	intNumber = input("Number %d: " % (i + 1))
	arrNumbers.append(int(intNumber))
arrNumbers.sort(reverse = True)
print("%d is the largest number provided." % arrNumbers[0])
#------------------------------------------------------------------
#Problem 2 - Print whether a year is a leap year
#----------------------------------------------------------------------

intYear = int(input("Enter a year: "))
if intYear <= 1500 or intYear >= 2200:
	print("Invalid Year")
elif intYear % 100 == 0:
	if intYear % 400 == 0:
		print("Yes, %d is a leap year." % intYear)
	else:
		print("No, %d is not a leap year." % intYear)
elif intYear % 4 == 0:
	print("Yes, %d is a leap year." % intYear)
else:
	print("No, %d is not a leap year." % intYear)
	
#----------------------------------------------------------------------
#Problem 3 - Print Net pay
#---------------------------------------------------------------------
dblRate = float(input("Enter your hourly pay rate: "))
dblHours = float(input("Enter hours worked: "))
if dblRate > 0 and dblHours > 0:
	dblGross = dblRate * dblHours
	if dblGross <= 300:
		dblTax = dblGross * 0.15
	elif dblGross <=450:
		dblTax = ((dblGross - 300) * 0.2) + 45
	else:
		dblTax = ((dblGross - 450) * .25) + 75
	dblNet = dblGross - dblTax
	print("Net pay: $%.2f" % dblNet)
else:
	print("Invalid input")