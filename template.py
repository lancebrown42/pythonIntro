# Name
# Assignment # 

#--------------------------------------------------------------------------
#   Assignment # Function Area
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
#1. Function Name:                Display instructions
#2. Function Description 
#--------------------------------------------------------------------------

Def yourfunctionname1( )
	Yourfunction statement 1
Yourfunction statement 2
Yourfunction statement 3
Yourfunction statement 4
	:
	:
	:

#--------------------------------------------------------------------------
#1. Function Name:                Display instructions
#2. Function Description 
#--------------------------------------------------------------------------

Def yourfunctionname2( )
	Yourfunction statement 1
Yourfunction statement 2
Yourfunction statement 3
Yourfunction statement 4
	:
	:
	:
#--------------------------------------------------------------------------
#1. Function Name:                Display instructions
#2. Function Description 
#--------------------------------------------------------------------------

Def yourfunctionname3( )
	Yourfunction statement 1
Yourfunction statement 2
Yourfunction statement 3
Yourfunction statement 4
	:
	:
	:



#--------------------------------------------------------------------------
# Assignment # Main Processing Area   - Example 1
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# Declare Variables
#--------------------------------------------------------------------------

intValue1 = int(0)
intValue2 = int(0)
strInputValidated = bool(False)


#--------------------------------------------------------------------------
# Declare Get and Validate Input
#--------------------------------------------------------------------------

while blnInputValidated == False:
   intValue1 = input("Enter Value 1: ")
   intValue1 = Validate_Integer_Input (intValue1) 
		:
		:
		:


#--------------------------------------------------------------------------
# Perform Calculations
#--------------------------------------------------------------------------

intValue2 = CalculateTotal( intValue1 )
		:
		:

#--------------------------------------------------------------------------
# Display Output
#--------------------------------------------------------------------------

PrintVolume(intValue1)
		:
		:
	

#--------------------------------------------------------------------------
# Assignment # Main Processing Area   - Example 2
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# Declare Variables
#--------------------------------------------------------------------------

intValue1 = int(0)
intValue2 = int(0)
blnInputValidated = bool(False)
strNewEmployee = str(‘Y’)



#--------------------------------------------------------------------------
# Loop for each employee – as an example
#--------------------------------------------------------------------------

while strNewEmployee == ‘Y’:

#--------------------------------------------------------------------------
# Declare Get and Validate Input
#--------------------------------------------------------------------------

while blnInputValidated == False:
  	 	intValue1 = input("Enter Value 1: ")
 	  	intValue1 = Validate_Integer_Input (intValue1) 
			:
			:
			:

	blnInputValidated = bool(False)


#--------------------------------------------------------------------------
# Perform Calculations
#--------------------------------------------------------------------------

intValue2 = CalculateTotal( intValue1 )
			:
			:

#--------------------------------------------------------------------------
# Display Output
#--------------------------------------------------------------------------

PrintVolume(intValue1)
			:
			:
	

#--------------------------------------------------------------------------
# Check for another employee
#--------------------------------------------------------------------------
while blnInputValidated == False:
		strNewEmployee = input("Another Employee: Y/N?")
 	  	strNewEmployee = Validate_String_Input (strNewEmployee) 
