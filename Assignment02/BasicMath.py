#--------------------------------------#
# Title: BasicMath.py
# Desc: This script file allows a user
#       to input their name and display
#       it back to them.
# Dev: NSmith
# Date: April 23, 2020
# Change Log: (who, when, what)
# NSmith, 2020-04-18, Created File
#--------------------------------------#

# Get User Input Data
strNum1 = input("Enter a first number: ")
strNum2 = input("Enter a second number: ")

#Process the Data
fltNum1 = float(strNum1)
fltNum2 = float(strNum2)
fltSum = fltNum1 + fltNum2
fltDiff = fltNum1 - fltNum2
fltProd = fltNum1 * fltNum2
fltQuot = fltNum1 / fltNum2

# Display the code
print('The sum of', fltNum1, 'and', fltNum2, 'is:', fltSum)
print('The difference of', fltNum1, 'and', fltNum2, 'is:', fltDiff)
print('The product of', fltNum1, 'and', fltNum2, 'is:', fltProd)
print('The quotient of', fltNum1, 'and', fltNum2, 'is:', fltQuot)

