#########################################################
#Lance Brown
#Project 1
#02/20/20
#########################################################



# -----------------------------------------------------------------
# Function Name:        GetValidInt
# Function Purpose:     Gets input from user and validates it
# -----------------------------------------------------------------
def GetValidInt():
	while True:
		try:
			intYears = int(input("Enter number of years worked: "))
		except ValueError:
			print("Please enter an integer")
			continue
		else:
			if ValidateInteger(intYears):
				return intYears
				break
			else:
				print("Please enter a valid integer")
				continue	



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
# Function Name:        GetValidFloat
# Function Purpose:     Gets input from user and validates it
# -----------------------------------------------------------------
def GetValidFloat(strPrompt):
	while True:
		try:
			dblOutput = float(input(strPrompt))
		except ValueError:
			print("Please enter a number")
			continue
		else:
			if ValidatePositive(dblOutput):
				return dblOutput
				break
			else:
				print("Please enter positive number")
				continue	



# -----------------------------------------------------------------
# Function Name:        Validate Positive
# Function Purpose:     Validates that inputs are positive
# -----------------------------------------------------------------
def ValidatePositive(*dblValuev):
	blnValid = False
	for dblValue in dblValuev:	
		if dblValue >= 0:
			blnValid = True
		else:
			return False
	return blnValid



# -----------------------------------------------------------------
# Function Name:        Get Boolean
# Function Purpose:     Converts user provided string into usable boolean
# -----------------------------------------------------------------
def GetBoolean(strPrompt):
	while True:
		strInput = input(strPrompt)
		if strInput == "No" or strInput == "no" or strInput == "n" or strInput == "N" or strInput == "NO":
			return False
			break
		elif strInput == "Yes" or strInput == "yes" or strInput == "y" or strInput == "Y" or strInput == "YES":
			return True
			break
		else:
			print("Please answer 'YES' or 'NO'")
			continue



# -----------------------------------------------------------------
# Function Name:        DiscountLookup
# Function Purpose:     Easy discount lookup
# -----------------------------------------------------------------
def DiscountLookup(intYears):
	if intYears <= 3:
		return 0.1
	elif intYears <= 6:
		return 0.14
	elif intYears <= 10:
		return 0.2
	elif intYears <= 15:
		return 0.25
	elif intYears > 15:
		return 0.3



# -----------------------------------------------------------------
# Function Name:        Manager Bonus
# Function Purpose:     Check if manager and adjust discount accordingly
# -----------------------------------------------------------------
def ManagerBonus(blnManager, dblDiscount):
	if blnManager:
		return (dblDiscount + 0.1)
	else:
		return dblDiscount



# -----------------------------------------------------------------
# Function Name:        Calculate YTD Discount
# Function Purpose:     Calculates discount dollars year to date
# -----------------------------------------------------------------
def CalculateYtdDiscount(dblPrevious, dblDiscount):
	return dblPrevious * dblDiscount



# -----------------------------------------------------------------
# Function Name:        Calculate Discount
# Function Purpose:     Calculates discount dollars on purchase
# -----------------------------------------------------------------
def CalculateDiscount(dblPurchase, dblDiscount, dblYtdDiscount):
	if dblYtdDiscount > 200:
		dblYtdDiscount = 200
	dblDiscountDollars = dblPurchase * dblDiscount
	if dblDiscountDollars + dblYtdDiscount >= 200:
		dblOverage = (dblDiscountDollars + dblYtdDiscount) - 200
		dblDiscountDollars -= dblOverage
	return dblDiscountDollars



# -----------------------------------------------------------------
# Function Name:        Main
# Function Purpose:     Controls flow of program
# -----------------------------------------------------------------
dblTotal = 0 #running total for session
dblDiscountTotal = 0 #running total with discounts
blnContinue = True #default state
while blnContinue == True: #controls prompts for additional employees
	print("***************************************\n***   Calculate employee discount   ***\n***************************************\n")
	intYears = GetValidInt()
	dblPrevious = GetValidFloat("Enter previous purchases: ")
	blnManager = GetBoolean("Is the employee a manager? Y/N: ")
	dblDiscount = ManagerBonus(blnManager, DiscountLookup(intYears))

	dblYtdDiscount = CalculateYtdDiscount(dblPrevious, dblDiscount)
	dblPurchase = GetValidFloat("How much is today's purchase? ")
	dblDiscountDollars = CalculateDiscount(dblPurchase, dblDiscount, dblYtdDiscount)
	dblDiscountPurchase = dblPurchase - dblDiscountDollars
	dblTotal += dblPurchase
	dblDiscountTotal += dblDiscountPurchase
	print("**********************************\n***   Transaction Summary   ***\n**********************************")
	print("Employee discount percentage: {:.0%} \nYear to date discount: ${:.2f} \nTotal before discount: ${:.2f} \nDiscount on this purchase: ${:.2f} \nTotal with discount: ${:.2f} \n".format(dblDiscount, dblYtdDiscount, dblPurchase, dblDiscountDollars, dblDiscountPurchase))
	blnContinue = GetBoolean("Calculate another discount? ")
print("**********************************\n***   All Employee Summary   ***\n**********************************")
print("Daily total before discounts: {:.2f} \nDaily total after discounts: {:.2f} \n".format(dblTotal, dblDiscountTotal))

	
