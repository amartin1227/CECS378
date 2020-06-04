#
#Author :   Alejandro Martin
#Class:     CECS378
#Due Date:  April 3, 2020
#Project:   Ultima V Program (Lab 2)
#
import time

#File path of the Ultima V file we are editing
filePath = "SAVED.GAM"

#dictionary of character names
cOrder = {1: "CREATED PLAYER", 2: "SHAMINO",
          3: "IOLO", 4: "MARIAH",
          5: "GEOFFREY", 6: "JAANA",
          7: "JULIA", 8: "DUPRE",
          9: "KATRINA", 10: "SENTRI",
          11: "GWENNO",  12: "JOHNE",
          13: "GORN", 14: "MAXWELL",
          15: "TOSHI", 16: "SADUJ"}

#dictionary of character offsets
cOffsets = {"CREATED PLAYER": int('0x02', 16), "SHAMINO": int('0x22', 16),
            "IOLO": int('0x42', 16), "MARIAH": int('0x62', 16),
            "GEOFFREY": int('0x82', 16), "JAANA": int('0xA2', 16),
            "JULIA": int('0xC2', 16), "DUPRE": int('0xE2', 16),
            "KATRINA": int('0x102', 16), "SENTRI": int('0x122', 16),
            "GWENNO": int('0x142', 16), "JOHNE": int('0x162', 16),
            "GORN": int('0x182', 16), "MAXWELL": int('0x1A2', 16),
            "TOSHI": int('0x1C2', 16), "SADUJ": int('0x1E2', 16)}

#dictionary of stats
sOrder = {1: "STRENGTH", 2: "INTELLIGENCE",
          3: "DEXTERITY", 4: "HP",
          5: "MAXHP", 6: "EXPERIENCE",
          7: "MAGIC"}

#dictionary of stats offsets
sOffsets = {"STRENGTH": int('0x0C', 16), "INTELLIGENCE": int('0x0E', 16),
            "DEXTERITY": int('0x0D', 16), "HP": int('0x10', 16),
            "MAXHP": int('0x12', 16), "EXPERIENCE": int('0x14', 16),
            "MAGIC": int('0x0F', 16)}

#dictionary of max values for stats
sMaxVal = {"STRENGTH": 255, "INTELLIGENCE": 255,
           "DEXTERITY": 255, "HP": 65535,
           "MAXHP": 65535, "EXPERIENCE": 65535,
           "MAGIC": 255}
 
#dictionary of items
iOrder = {1: "GOLD", 2: "KEYS",
          3: "SKULL KEYS", 4: "GEMS",
          5: "BLACK BADGE", 6: "MAGIC CARPET",
          7: "MAGIC AXE"}

#dictionary of item offsets
iOffsets = {"GOLD": int('0x204', 16), "KEYS": int('0x206', 16),
            "SKULL KEYS": int('0x20B', 16), "GEMS": int('0x207', 16),
            "BLACK BADGE": int('0x218', 16), "MAGIC CARPET": int('0x20A', 16),
            "MAGIC AXE": int('0x240', 16)}

#dictionary of max values for items
iMaxVal = {"GOLD": 65535, "KEYS": 255,
           "SKULL KEYS": 255, "GEMS": 255,
           "BLACK BADGE": 255, "MAGIC CARPET": 255,
           "MAGIC AXE": 255}
#
#This function is for the main menu when the user runs the program
#This helps navigate the user to either edit character stats, inventory,
#or just to save and exit the program.
#
def mainMenu(data):
    #main menu of program
    print("------------------------------------------------------------------------")
    print("")
    print("Hello fellow gamer, welcome to this editing program for Ultima V!!")
    print("Please keep this program on the hush hush (shhhhhhh)")
    print("NOTE** All editing for SAVED.GAM file will be dealt by using hexadecimals.")
    print("")
    print("\t\tWhat would you like to alter?")
    print("")
    print("------------------------------------------------------------------------\n")
    print("1. Character Stats")
    print("2. Item Inventory of Character(Gold, Keys, Gems, Badges, Carpets, Axes")
    print("3. Save your edits and EXIT\n")
    #input from user is assigned to selection
    selection = input()
    print("")
    #if user selection is not one of 3 options, ask user to choose again
    while(selection != "1" and selection != "2" and selection != "3"):
        selection = input("Please make a valid selection as your selection was invalid(1, 2, or 3): \n")
    #if selection 1 is chosen, then it goes to editCharacter function
    if(selection == "1"):
        editCharacter(data)
    #if selection 2 is chosen, then it goes to editInventory function
    elif(selection == "2"):
        editInventory(data)
    #if selection 3 is chosen, then it goes to writeData function, writes to the file any changes made
    #then saves the SAVED.GAM file and ends program
    else:
        print("Please wait as I am saving your updated work")
        #pauses program for 2 seconds
        time.sleep(2)
        print("File will be fully saved and read to go in...")
        #pauses program for 2 seconds
        time.sleep(2)
        print("3")
        #pauses program for 2 seconds
        time.sleep(2)
        print("2")
        #pauses program for 2 seconds
        time.sleep(2)
        print("1")
        #pauses program for 3 seconds
        time.sleep(3)
        #goes to writeData function
        writeData(data)
        print("Congrats, you have a new saved file. Now get back into the game and enjoy!\n")

#
#This function opens the file from filepath above
#then it reads the binary data from file
#then it closes the file
#
def readData():
    with open(filePath, "rb") as save:
        dataBytes = list(bytearray(save.read()))
        #file closes
        save.close()
        #returns databytes value
        return dataBytes

#
#This function allows user to edit stats for the whichever player(s) of Ultima V they choose
#
def statEdit(character, data):
    #prints which character to edit their stats
    print("")
    print("Which stat would you like to alter for {}?\n".format(
        cOrder[character]))
    print("")
    #prints which stat of the character selected to edit
    print("1.  {}\n2.  {}\n3.  {}\n4.  {}\n5.  {}\n6.  {}\n7.  {}".format(sOrder[1], sOrder[2], sOrder.get(3), sOrder.get(4),
                                                                          sOrder[5], sOrder[6], sOrder[7]))
    print("")
    #loops continuously as long as boolean value is True
    while(True):
        try:
            #cast user input as an int and assigns value to selection
            selection = int(input())
        #throws error message if wrong type of value is passed through(ex. char, boolean)
        except ValueError:
            print("Please select a valid choice (1 - 7) for your character selection: \n")
            continue
        #throws error message if wrong integer value is passed through(ex. -4, 100)
        if(selection < 1 or selection > 7):
            print("Please select a valid choice (1 - 7) for your character selection: \n")
            continue
        else:
            break
    #sets the user's selection of character's stat to statName
    statName = sOrder[selection]
    #sets the index value of the selected character's stat offset to index variable
    index = sOffsets[statName] + cOffsets[cOrder[character]]
    #sets the max value of selected character's stat to maxVal variable
    maxVal = sMaxVal[statName]
    #if maxVal is less than 256, sets index value to currVal
    if(maxVal < 256):
        currVal = data[index]
    #otherwise, sets currVal to 0
    else:
        currVal = 0
    #loops continuously as long as boolean value is True
    while(True):
        try:
            #casts new value of selected character's stats user wants to change to integer value
            #and then sets it to chosen variable
            print("")
            chosen = int(input("Current value for {} {} is {}. Please enter a value from 0 - {} to alter {} {}: \n".format(
                cOrder[character], statName, data[index], maxVal, cOrder[character], statName)))
        #throws error message if wrong type of value is passed through(ex. char, boolean)
        except ValueError:
            print(
                "Please choose a number 0 - {} to confirm your character selection\n".format(maxVal))
            continue
        #throws error message if wrong integer value is passed through integer range
        if(chosen < 0 or chosen > maxVal):
            print(
                "Please choose a number 0 - {} to confirm your character selection\n".format(maxVal))
            continue
        else:
            break
    #sets counter to 0
    counter = 0
    #sets converted chosen int value to bytes
    #then gets most significant byte at end of array
    #then converts it all to a list and sets it to bArray
    bArray = list(bytearray((chosen).to_bytes(2, byteorder="little")))
    #if length of bArray list is 1, then insert (0,0) into the bArray
    if(len(bArray) == 1):
        bArray.insert(0, 0)
    #iterates through the n amount of items in bArray list
    for n in bArray:
        data[index + counter] = n
        #increments counter by 1
        counter += 1
    #prints out updated characters stat to chosen user input value
    print("{} {} has been updated to {}".format(cOrder[character], statName, chosen))
    selection = input(
        "Would you like to alter another stat? Enter Y or N :\n")
    #if user input does not match "y" or "n", ask user to choose again
    while((selection.lower() != "y" and selection.lower() != "n")):
        selection = input(
            "I am sorry but that choice is invalid. Please choose a proper choice (1 or 2): \n")
    #if "y" is chosen, then program runs through this statEdit function again
    if(selection.lower() == "y"):
        statEdit(character, data)

#
#This function allows user to select which character they would like to alter
#
def characterSelect(data):
    #Displays character list to user for their selection
    print("****************************************************************************")
    print("You have come to character selection.")
    print("Please choose character from list below that you would like to alter?")
    print("1.  {}\n2.  {}\n3.  {}\n4.  {}\n5.  {}\n6.  {}\n7.  {}\n8.  {}".format(cOrder[1], cOrder[2], cOrder[3], cOrder[4],
                                                                                  cOrder[5], cOrder[6], cOrder[7], cOrder[8]))
    print("9.  {}\n10. {}\n11. {}\n12. {}\n13. {}\n14. {}\n15. {}\n16. {}".format(cOrder[9], cOrder[10], cOrder[11], cOrder[12],
                                                                                  cOrder[13], cOrder[14], cOrder[15], cOrder[16]))
    print("")
    #loops continuously as long as boolean value is True
    while(True):
        try:
            #cast user input as an int and assigns value to selection
            selection = int(input())
            print("")
        #throws error message if wrong type of value is passed through(ex. char, boolean)
        except ValueError:
            print("I am sorry but you made an invalid choice. Please select a number (1 - 16) from the game's character selection\n")
            continue
        #throws error message if wrong integer value is passed through integer range
        if(selection < 1 or selection > 16):
            print("I am sorry but you chose an invalid character choice. Please select a number (1 - 16) from the game's character selection\n")
            continue
        else:
            break
    #program takes user selection and data and passes it through statEdit function
    statEdit(selection, data)
    print("")
    selection = input(
        "Would you like to alter another character? Enter Y or N :\n")
    print("")
    #if user input does not match "y" or "n", ask user to choose again
    while((selection.lower() != "y" and selection.lower() != "n")):
        selection = input(
            "I am sorry but that choice is invalid. Please choose a proper choice (Y or N):\n")
    #if "y" is chosen, then program runs through this characterSelect function again
    if(selection.lower() == "y"):
        characterSelect(data)

#
#This function runs when user selects option 1 from main menu
#Once selected, it then goes to characterSelect function
#Once character is edited, then prints out message returning to main menu
#
def editCharacter(data):
    #goes to characterSelect function
    characterSelect(data)
    print("Returning you to the Main Menu\n")
    #returns to mainMenu function
    mainMenu(data)

#
#This function allows user to edit the amount of selected item they choose
#
def itemTotalEdit(item, data):
    #sets the user's index selection of item chosen to itemName
    itemName = iOrder[item]
    #sets the user's offset of itemName selection chosen to index
    index = iOffsets[itemName]
    #sets the max value of selected item to maxVal variable
    maxVal = iMaxVal[itemName]
    #set hex value of currVal of item
    if(maxVal > 255 and data[index] > 0):
        currVal = int(hex(data[index])[2:] + hex(data[index + 1])[2:], 16)
    #otherwise index gets incremented by 1 and assigned to currVal
    elif(maxVal > 255 and data[index] == 0):
        currVal = data[index + 1]
    else:
        currVal = data[index]
    #loops continuously as long as boolean value is True
    while(True):
        try:
            #casts new value of selected inventory stats user wants to change to integer value
            #and then sets it to chosen variable
            print("")
            chosen = int(input("Current amount of {} in inventory is {}. Please enter a value from 0 - {} to alter: \n".format(
                itemName, currVal, maxVal)))
        #throws error message if wrong type of value is passed through(ex. char, boolean)
        except ValueError:
            print(
                "Please choose a number 0 - {} to confirm your amount\n".format(maxVal))
            continue
        #throws error message if wrong integer value is passed through integer range
        if(chosen < 0 or chosen > maxVal):
            print(
                "Please choose a number 0 - {} to confirm your amount\n".format(maxVal))
            continue
        else:
            break
    #sets counter to 0
    counter = 0
    #sets converted chosen int value to bytes
    #then gets most significant byte at end of array
    #then converts it all to a list and sets it to bArray
    bArray = list(bytearray((chosen).to_bytes(2, byteorder="little")))
    #if length of bArray list is 1, then insert (0,0) into the bArray
    if(len(bArray) == 1):
        bArray.insert(0, 0)
    #iterates through the n amount of items in bArray list
    for n in bArray:
        data[index + counter] = n
        #increments counter by 1
        counter += 1
    #prints out updated item inventory stat to chosen user input value
    print("")
    print("Number of {} has been updated to {}".format(itemName, chosen))
    print("")
    selection = input(
        "Would you like to alter another amount? Enter Y or N \n")
    #if user input does not match "y" or "n", ask user to choose again
    while((selection.lower() != "y" and selection.lower() != "n")):
        selection = input(
            "I am sorry but that choice is invalid. Please choose a proper choice (Y or N):\n")
    #if "y" is chosen, then program runs through this itemSelect function again
    if(selection.lower() == "y"):
        itemSelect(data)

#
#This function allows user to select which item they would like to alter
#
def itemSelect(data):
    #Displays item list to user for their selection
    print("****************************************************************************")
    print("Which item would you like to alter?\n")
    print("1.  {}\n2.  {}\n3.  {}\n4.  {}\n5.  {}\n6.  {}\n7.  {}".format(iOrder[1], iOrder[2], iOrder[3], iOrder[4],
                                                                          iOrder[5], iOrder[6], iOrder[7]))
    print("")
    #loops continuously as long as boolean value is True
    while(True):
        try:
            #cast user input as an int and assigns value to selection
            selection = int(input())
        #throws error message if wrong type of value is passed through(ex. char, boolean)
        except ValueError:
            print("I am sorry but you made an invalid choice. Please choose a number (1 - 7) to confirm your item selection\n")
            continue
        #throws error message if wrong integer value is passed through integer range
        if(selection < 1 or selection > 7):
            print("I am sorry but you made an invalid choice. Please Select A Number 1 - 7 to Confirm Your Item selection\n")
            continue
        else:
            break
    #goes to itemTotalEdit function
    itemTotalEdit(selection, data)

#
#This function runs when user selects option 2 from main menu
#Once selected, it then goes to itemSelect function
#Once inventory item is edited, then prints out message returning to main menu
#
def editInventory(data):
    #goes to itemSelect function
    itemSelect(data)
    print("Returning you to the Main Menu\n")
    #returns to mainMenu function
    mainMenu(data)

#
#This function overwrites current data in file
#and writes updated data to the file from filepath above
#then it closes the file
#
def writeData(data):
    with open(filePath, "wb") as save:
        save.write(bytearray(data))
        #then it closes the file
        save.close()

#executes this line and goes to mainMenu function once program is run
if __name__ == "__main__":
    #runs mainMenu function
    mainMenu(readData())
