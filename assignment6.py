#########################################################
#Lance Brown
#Assignment 6
#02/12/20
#########################################################

# -----------------------------------------------------------------
# Function Name:        Display Instructions
# Function Purpose:     Displays instructions to the user
# -----------------------------------------------------------------
def DisplayInstructions():
	print("This program will demonstrate how to make and use procedures in Python... \n In addition it will demonstrate how to pass values and variables into \n a procedure as parameters.  It will demonstrate Python deals with ByRef and ByVal.")
	return



# -----------------------------------------------------------------
# Function Name:        Validate Integer
# Function Purpose:     Validates that inputs are positive integers
# -----------------------------------------------------------------
def ValidateInteger(*intValuev):
	blnValid = False
	for intValue in intValuev:	
		if intValue > 0 and isinstance(intValue, int):
			blnValid = True
		else:
			return False
	return blnValid



# -----------------------------------------------------------------
# Function Name:        Display Message
# Function Purpose:     Displays a set message a given number of times
# -----------------------------------------------------------------
def DisplayMessage(intPrintCount):
	for i in range(intPrintCount):
		print("I Love Python\n")
	return
		
		

# -----------------------------------------------------------------
# Function Name:        Get Larger Value
# Function Purpose:     Finds the larger of two values
# -----------------------------------------------------------------
def GetLargerValue(intValue1, intValue2):
	if intValue1 > intValue2:
		return intValue1
	elif intValue2 > intValue1:
		return intValue2
	elif intValue1 == intValue2:
		return intValue1
	else:
		print("Something has gone horribly wrong")
		return



# -----------------------------------------------------------------
# Function Name:        Get Largest Value
# Function Purpose:     Finds the largest of seven values
# -----------------------------------------------------------------
def GetLargestValue(intValue1, intValue2, intValue3, intValue4, intValue5, intValue6, intValue7):
	intMax = GetLargerValue(intValue1, intValue2)
	intMax = GetLargerValue(intMax, intValue3)
	intMax = GetLargerValue(intMax, intValue4)
	intMax = GetLargerValue(intMax, intValue5)
	intMax = GetLargerValue(intMax, intValue6)
	intMax = GetLargerValue(intMax, intValue7)
	return intMax



# -----------------------------------------------------------------
# Function Name:        Calculate Sphere Volume
# Function Purpose:     Calculates volume of a sphere from given diameter
# -----------------------------------------------------------------
def CalculateSphereVolume(intDiameter):
	dblVolume = (4 / 3) * 3.1415 * (intDiameter / 2) ** 3
	return dblVolume



# -----------------------------------------------------------------
# Function Name:        Main
# Function Purpose:     Controls flow of program
# -----------------------------------------------------------------
DisplayInstructions()
intPrintCount = int(input("Enter print count: "))
if ValidateInteger(intPrintCount):
	DisplayMessage(intPrintCount)
else:
	print("Invalid input")
intValue1, intValue2 = input("Enter two positive integers: ").split()
if ValidateInteger(int(intValue1), int(intValue2)):
	print(GetLargerValue(int(intValue1), int(intValue2)))

else:
	print("Invalid input")
intValue1, intValue2, intValue3, intValue4, intValue5, intValue6, intValue7 = input("Enter seven positive integers: ").split()
if ValidateInteger(int(intValue1), int(intValue2), int(intValue3), int(intValue4), int(intValue5), int(intValue6), int(intValue7)):
	print(GetLargestValue(int(intValue1), int(intValue2), int(intValue3), int(intValue4), int(intValue5), int(intValue6), int(intValue7)))
else:
	print("Invalid input")
intDiameter = int(input("Enter the diameter of a sphere: "))
if ValidateInteger(intDiameter):
	print(CalculateSphereVolume(intDiameter))
else:
	print("Invalid input")
