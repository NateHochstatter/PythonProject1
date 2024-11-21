from JsonStuff import *
from checkAll import *
# A file containing functions regarding the pages

# A basic function that prints the requested page
def printPage(filename):
    inputFile = open(filename, 'r') #Get the file text
    print(inputFile.read()) #Print the file text
    inputFile.close() #Close the connection

#Function for the start screen page
def startPage():

    #If statement and while loop to keep the program running until they select the leave option and confirm
    ex = False
    while (ex != True):
        printPage("Welcome.txt")  # print the welcome text
        choice = input(str("Please Enter the Operation Code: "))  # get the users choice
        while (choice != "6"):
            #if statements for each option and the function correlating to them
            if (choice == "1"):
                addStudentPage()
            elif (choice == "2"):
                deleteStudentPage()
            elif (choice == "3"):
                modifyStudentPage()
            elif (choice == "4"):
                displayStudentPage()
            elif (choice == "5"):
                displayAllPage()
            else:
                print("Wrong input enter a valid number") #error message
            printPage("Welcome.txt") #Once the chosen function is done start the process again
            choice = input(str("Please Enter the Operation Code: "))
        leave = input(str("Do you want to Exit the System? Enter Y to Confirm: "))
        if (leave.upper() == "Y"):
            ex = True

#Function for adding a student to the json
def addStudentPage():
    printPage("AddStudent.txt") #Print the addStudent text
    finalcheck = True #Check for if the item already exists so it just stops and goes back to the start page
    check = True #check so it goes through the while loop until a valid id is given

    #the following series of while loops get a part of the students info only stopping if they get a valid input
    #or if the info already exists
    while check and finalcheck:
        Id = str(input("Please enter the student ID: "))
        if checkValID(Id):
            if IDExists(Id):
                print("\u274c Student ID already exists in the system. Please enter a different Id")
                finalcheck = False
            else:
                check = False
        else:
            print(f"\u274c Invalid Student ID")

    check = True
    while check and finalcheck:
        Name = str(input("Please enter the student Name: "))
        if checkName(Name):
            if NameExists(Name):
                print("\u274c Student Name already exists in the system. Please enter a different Name")
                finalcheck = False
            else:
                check = False
        else:
            print(f"\u274c Invalid Student Name")

    check = True
    while check and finalcheck:
        Phone = str(input("Please enter the student Phone: "))
        if checkPhone(Phone):
            if PhoneExists(Phone):
                print("\u274c Student Phone already exists in the system. Please enter a different Phone")
                finalcheck = False
            else:
                check = False
        else:
            print(f"\u274c Invalid Student Phone")

    check = True
    while check and finalcheck:
        Major = str(input("Please enter the student Major: "))
        if checkMaj(Major):
            check = False
        else:
            print(f"\u274c Invalid Student Major")


    if finalcheck: #if none of the info already exists then complete the task
        #Format the data collected before sending it to the function
        newStudent = {
            "ID": Id,
            "Name": Name,
            "Phone": Phone,
            "Major": Major.upper()}

        # put the data into the function and print that the program was a success
        addStudent(newStudent)
        print("\u2714 New student record has been added")

def deleteStudentPage():
    #Prompt the user to enter a student ID to delete
    IDInput = input("Please enter a Student ID to delete: ")

    #Checks to make sure that the ID exists
    if IDExists(IDInput) == True:
        #Display student information
        printPage("StudentRecord.txt")
        displayStudent(IDInput)

        #Verify that the user wants to delete the student
        response = input("Are you sure you want to delete this student from the record? Y or N: ")

        #Yes
        if response.lower() == "y":
            deleteStudent(IDInput)
            print(f"Student {IDInput} has been deleted")
        #No
        elif response.lower() == "n":
            print(f"Student {IDInput} has not been deleted")
        #Invalid responses
        else:
            print("INVALID RESPONSE")
    #ID does not exist
    else:
        print(f"\u274c The student Id {IDInput} does not exist")
# The function for if option 5 is selected to display all students
def displayAllPage():
    #Simple function with me just printing the record text before calling the display function
    printPage("StudentRecord.txt")
    displayAll()

#A function for choice 4 to go through the steps of getting the student id and then displaying that student
def displayStudentPage():
    Id = str(input("Please enter the student ID: ")) #Get the id
    printPage("StudentRecord.txt") #print the record text
    if checkValID(Id): #if statements to ensure the id is both valid and existing
        if IDExists(Id):
            displayStudent(Id) #call the displayStudent function with the given id
        else:
            print(f"\u274c The student Id {Id} does not exist") #error messages for if it is invalid or nonexistent
    else:
        print(f"\u274c The student Id {Id} is not valid")

#a function for choice 3 for selecting a student and then modifying their data
def modifyStudentPage():
    #starts off by basically doing the displayStudent function but with a key change of setting a
    # check to false if there is an issue
    Id = str(input("Please enter the student ID: "))
    greatCheck = True #check for if there is an issue with the id which means it should stop
    # trying to modify something
    printPage("StudentRecord.txt")
    if checkValID(Id):
        if IDExists(Id):
            displayStudent(Id)
        else:
            print(f"\u274c The student Id {Id} does not exist")
            greatCheck = False
    else:
        print(f"\u274c The student Id {Id} is not valid")
        greatCheck = False

    if greatCheck: #if there were no issues continue as normal

        #A series of while loops that until a valid new data is given
        check = True
        while check:
            newName = str(input("New Name: "))
            if newName == "" or checkName(newName): #It is ok if the data is left empty or is just a valid name
                check = False
            else:
                print(f"\u274c Invalid Student Name")

        check = True
        while check:
            newPhone = str(input("New Phone: "))
            if newPhone == "" or checkPhone(newPhone):
                check = False
            else:
                print(f"\u274c Invalid Student Phone")

        check = True
        while check:
            newMajor = str(input("New Major: "))
            if newMajor == "" or checkMaj(newMajor):
                check = False
            else:
                print(f"\u274c Invalid Student Major")

        if newName == "" and newPhone == "" and newMajor == "": #If they left all the inputs empty
            # send an error message
            print("\u274c Record not modified")
        else:
            #otherwise call the function and say things went well
            modifyStudent(Id, newName, newPhone, newMajor.upper())
            print("\u2714 Student record updated successfully")
