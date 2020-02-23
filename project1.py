#########################################################
#Lance Brown
#Project 1
#02/20/20
#########################################################
# -----------------------------------------------------------------
# Function Name:        Convert Boolean
# Function Purpose:     Converts user provided string into predictable boolean
# -----------------------------------------------------------------
def ConvertBoolean(strInput):
	if strInput == "No" or strInput == "no" or strInput == "n" or strInput == "N":
		return False
	if strInput == "Yes" or strInput == "yes" or strInput == "y" or strInput == "Y":
		return true



# -----------------------------------------------------------------
# Function Name:        Main
# Function Purpose:     Controls flow of program
# -----------------------------------------------------------------
blnContinue = True #default state
while blnContinue == True: #controls prompts for additional employees
	print("********************\n***   Calculate employee discount   ***\n********************\n")
	intYears = int(input("Enter number of years worked: "))
	dblPrevious = float(input("Enter previous purchases: "))
	strManager = input("Is the employee a manager? Y/N: ")
	blnManager = ConvertBoolean(strManager)
	dblPurchase = float(input("How much is today's purchase? "))
	strContinue = input("Calculate another discount? ")
	blnContinue = ConvertBoolean(strContinue)
	
	
