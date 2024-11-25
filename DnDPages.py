from JsonStuffDnD import *
from checkAll import *

def printPage(filename):
    inputFile = open(filename, 'r') #Get the file text
    print(inputFile.read()) #Print the file text
    inputFile.close()

def startPage():
    #If statement and while loop to keep the program running until they select the leave option and confirm
    ex = False
    while (ex != True):
        printPage("WelcomeDnD.txt")  # print the welcome text
        choice = input(str("Please Enter the Operation Code: "))  # get the users choice
        while (choice != "6"):
            #if statements for each option and the function correlating to them
            if (choice == "1"):
                #addCharacterPage()
            elif (choice == "2"):
                #deleteCharacterPage()
            elif (choice == "3"):
                #modifyCharacterPage()
            elif (choice == "4"):
                #displayCharacterPage()
            elif (choice == "5"):
                #displayAllPage()
            else:
                print("Wrong input enter a valid number") #error message
            printPage("WelcomeDnD.txt") #Once the chosen function is done start the process again
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

def deleteCharacterPage():
    printPage("DeleteCharacter.txt")
    #Prompt the user to enter a student ID to delete
    IDInput = input("Please enter a Student ID to choose from: ")
    CharID = input("Please enter a Character ID to choose from: ")

    #Checks to make sure that the ID exists
    if IDExists(IDInput) == True:
        if(CharIDExists(CharID)):
            
            printPage("StudentRecord.txt")
            displayStudent(IDInput)
    
            #Verify that the user wants to delete the student
            response = input("Are you sure you want to delete this character from the record? Y or N: ")
    
            #Yes
            if response.lower() == "y":
                deleteCharacter(CharID)
                print(f"Character {CharID} has been deleted")
            #No
            elif response.lower() == "n":
                print(f"Character {CharID} has not been deleted")
            #Invalid responses
            else:
                print("INVALID RESPONSE")
        else:
            print(f"\u274c The character Id {CharID} does not exist")
    #ID does not exist
    else:
        print(f"\u274c The student Id {IDInput} does not exist")
def CharIDExists(ID, filename="characterData.json"):
    with open(filename, 'r') as file:
        data = json.load(file)
        for characters in data:
            if character["ID"] == ID:
                return True
    return False 
