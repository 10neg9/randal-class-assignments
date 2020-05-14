# --------------------------------------#
# Title: HomeInventory.py
# Desc: Script asks a user for the name of
#       a household item and its estimated
#       value and then stores the data to
#       a text file and notifies user that
#       the data was saved.
# Dev: NSmith
# Date: May 3, 2020
# Change Log: (who, when, what)
# NSmith, 2020-05-03, Created File
# --------------------------------------#

# Get user input, ask for household item
strItem = input('Enter a Item: ')

# Get user input, ask for estimated value
strVal = input('Enter a Estimated Value: ')

# Process the data
strData = strItem + ',' + strVal + '\n'

# Open file
objFile = open("C:\_PythonClass\Assignment03\HomeInventory.txt", "a")

# Write to file
objFile.write(strData)

# Close file
objFile.close()

# Display message to user
print('Data saved to file!')
