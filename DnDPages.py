def startPage():
    #If statement and while loop to keep the program running until they select the leave option and confirm
    ex = False
    while (ex != True):
        printPage("Welcome.txt")  # print the welcome text
        choice = input(str("Please Enter the Operation Code: "))  # get the users choice
        while (choice != "6"):
            #if statements for each option and the function correlating to them
            if (choice == "1"):
                addCharacterPage()
            elif (choice == "2"):
                deleteCharacterPage()
            elif (choice == "3"):
                modifyCharacterPage()
            elif (choice == "4"):
                displayCharacterPage()
            elif (choice == "5"):
                displayAllPage()
            else:
                print("Wrong input enter a valid number") #error message
            printPage("Welcome.txt") #Once the chosen function is done start the process again
            choice = input(str("Please Enter the Operation Code: "))
        leave = input(str("Do you want to Exit the System? Enter Y to Confirm: "))
        if (leave.upper() == "Y"):
            ex = True


def addCharacterPage():
    printPage("AddCharacter.txt")
    finalcheck = True
    check = True
    while check and finalcheck:
        Id = str(input("Please enter the character ID: "))
        if checkValID(Id):
            if CharIDExists(Id):
                print("\u274c Character ID already exists in the system. Please enter a different Id")
                finalcheck = False
            else:
                check = False
        else:
            print(f"\u274c Invalid Charcter ID")

    Name = str(input("Please enter the Character Name: "))

    check = True
    while check and finalcheck:
        Class = str(input("Please enter the Character Class: "))
        if checkClass(Class):
            check = False
        else:
            print(f"\u274c Invalid Character Class")

    check = True
    while check and finalcheck:
        Level = input(int("Please enter the Character Level: "))
        if checkLevel(Level):
            check = False
        else:
            print(f"\u274c Invalid Character Level")

    check = True
    while check and finalcheck:
        Race = str(input("Please enter the Character Race: "))
        if checkRace(Race):
            check = False
        else:
            print(f"\u274c Invalid Character Race")

    Campaign = str(input("Please enter the Campaign: "))

    if finalcheck:
        newCharacter = {
            "ID": Id,
            "Name": Name,
            "Class": Class,
            "Level": Level,
            "Race": Race,
            "Campaign": Campaign}

        addCharacter(newCharacter)
        print("\u2714 New Character record has been added")
  
