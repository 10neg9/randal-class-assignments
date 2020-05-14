# --------------------------------------#
# Title: HomeInventory.py
# Desc: This script prints a menu to a user,
#       the user selects a menu item, and based
#       on the menu item chosen by the user the
#       script will perform one of the three
#       menu options: take data from the user
#       and store is in a list, or display the
#       current data, or exit with the option
#       to save the list to a text file.
# Dev: NSmith
# Date: May 7, 2020
# Change Log: (who, when, what)
# NSmith, 2020-05-07, Created File
# Nsmith, 2020-05-10, Changed variable name list to listTable
# --------------------------------------#

# Step 1
# Display a menu of choices to the user
# ("Add Data to List", "Display Current Data", "Exit and Save File")
listTable = []  # initialize the list
while (True):
    print("\n\tMenu of Options")
    print("\t1) Add Data to a List")
    print("\t2) Display Current Data")
    print("\t3) Exit and Save to File")
    strOption = input("\nWhich option would you like to perform? [1 - 3]: ")

    # Step 2
    # Add a new item to the List(Table) each time the user makes that choice
    if strOption == '1':
        listVal = [(input('Enter an Item: ')), \
                   (input('Enter an Estimated Value: '))]
        listTable += [listVal]

    # Step 3
    # Display the data in the List(Table) each time the user makes that choice
    elif strOption == '2':
        print(listTable)

    # Step 4
    # Exit the program and save the data to a text file when the user makes that choice
    elif strOption == '3':
        while (True):
            print("Would you like to save your Data?")
            strChoice = input("Enter 'y' or 'n': ")
            if strChoice.lower() == 'n':
                break  # end this nested while loop
            elif strChoice.lower() == 'y':
                objFile = open("HomeInventory.txt", "w")  # Open file
                # iterate through the rows in the list and
                # write elements of the rows to the file
                for row in listTable:
                    objFile.write(row[0] + "," + row[1] + '\n')
                objFile.close()  # Close file
                break  # end this nested while loop
            else:
                print("\nNot an option! Please try again...")
        break  # end the while loop, i.e. end the script
    else:
        print("\nNot an option! Please try again...")
