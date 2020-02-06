#--------------------------------------------
#Lance Brown
#Assignment 5
#---------------------------------------------

#-----------------------------------------------
#For loop
#------------------------------------------------
dblRate = float(input("Enter your current hourly pay: "))
dblRaise = float(input("Enter your expected annual raise percentage: "))
dblAnnual = dblRate * 40 * 52
for i in range(10):
	print("Year %d - $%.2f" % ((i+1), dblAnnual))
	dblAnnual *= 1 + (dblRaise * 0.01)
	
#---------------------------------------------------------------
#While Loop
#-------------------------------------------------------
dblRate = float(input("Enter your current hourly pay: "))
dblRaise = float(input("Enter your expected annual raise percentage: "))
dblAnnual = dblRate * 40 * 52
i = 0
while i < 10:
	print("Year %d - $%.2f" % ((i+1), dblAnnual))
	dblAnnual *= 1 + (dblRaise * 0.01)
	i+=1