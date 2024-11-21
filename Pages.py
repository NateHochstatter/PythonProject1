from JsonStuff import *
from checkAll import *
# A file containing functions regarding the pages

# A basic function that prints the requested page
def printPage(filename):
    inputFile = open(filename, 'r')
    print(inputFile.read())
    inputFile.close()

def startPage():
    printPage("Welcome.txt")
    choice = input(str("Please Enter the Operation Code: "))

    ex = False
    if (ex != True):
        while (choice != "6"):
            if (choice == "1"):
                addStudentPage()
            elif (choice == "2"):
                print()
            elif (choice == "3"):
                modifyStudentPage()
            elif (choice == "4"):
                displayStudentPage()
            elif (choice == "5"):
                displayAllPage()
            else:
                print("Wrong input enter a valid number")
            printPage("Welcome.txt")
            choice = input(str("Please Enter the Operation Code: "))
        leave = input(str("Do you want to Exit the System? Enter Y to Confirm: "))
        if (leave == "Y"):
            ex = True

#Incomplete
def addStudentPage():
    printPage("AddStudent.txt")
    finalcheck = True
    check = True
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


    if finalcheck:
        newStudent = {
            "ID": Id,
            "Name": Name,
            "Phone": Phone,
            "Major": Major}

        addStudent(newStudent)
        print("\u2714 New student record has been added")
    #startPage()

def deleteStudentPage():
    #Prompt the user to enter a student ID to delete
    IDInput = input("Please enter a Student ID to delete: ")

    #Checks to make sure that the ID exists
    #ID Exists
    if IDExists(IDInput) == True:
        #Display student information
        print("=====Student Record=====")
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
        print("Student ID does not exist")
# The function for if option 5 is selected to display all students
def displayAllPage():
    printPage("StudentRecord.txt")
    displayAll()
    #startPage()

#A function for choice 4 to go through the steps of getting the student id and then displaying that student
def displayStudentPage():
    Id = str(input("Please enter the student ID: "))
    printPage("StudentRecord.txt")
    if checkValID(Id):
        if IDExists(Id):
            displayStudent(Id)
        else:
            print(f"\u274c The student Id {Id} does not exist")
    else:
        print(f"\u274c The student Id {Id} is not valid")
    #startPage()

def modifyStudentPage():
    Id = str(input("Please enter the student ID: "))
    greatCheck = True
    printPage("StudentRecord.txt")
    if checkValID(Id):
        if IDExists(Id):
            displayStudent(Id)
        else:
            print(f"\u274c The student Id {Id} does not exist")
            greatCheck = False
            #startPage()
    else:
        print(f"\u274c The student Id {Id} is not valid")
        greatCheck = False
        #startPage()

    if greatCheck:
        check = True
        while check:
            newName = str(input("New Name: "))
            if newName == "" or checkName(newName):
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

        if newName == "" and newPhone == "" and newMajor == "":
            print("\u274c Record not modified")
        else:
            modifyStudent(Id, newName, newPhone, newMajor.upper())
            print("\u2714 Student record updated successfully")
