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
            inputFile = open("Welcome.txt", 'r')
            print(inputFile.read())
            choice = input(str("Please Enter the Operation Code: "))
        leave = input(str("Do you want to Exit the System? Enter Y to Confirm: "))
        if (leave == "Y"):
            ex = True

#Incomplete
def addStudentPage():
    printPage("AddStudent.txt")
    ID = getId()
    # 2 placeholders
    Name = "test1"
    Phone = "test1"
    #Name = getName()
    #Phone = getPhone()
    Major = getMajor()

    newStudent = {
        "ID": ID,
        "Name": Name,
        "Phone": Phone,
        "Major": Major}

    addStudent(newStudent)
    print("\u2714 New student record has been added")
    startPage()

#Note for all the get functions below I haven't decided if I
#want to do this format or the format done for modify students
#function to ask for an id until they give a valid answer
def getId():
    Id = str(input("Please enter the student ID: "))
    if checkValID(Id):
        if IDExists(Id):
            print("\u274c Student ID already exists in the system. Please enter a different Id")
            startPage()
        else:
            return Id
    else:
        print(f"\u274c Invalid Student ID")
        getId()

#function to ask for a name until they give a valid answer (waiting for checkName)
'''
def getName():
    Name = str(input("Please enter the student name (Firstname Lastname: "))
    if checkName(Name):
        if NameExists(Name):
            print("\u274c Student Name already exists in the system. Please enter a different Name")
            startPage()
        else:
            return Name
    else:
        print(f"\u274c Invalid Student Name")
        getName()
'''

#function to ask for a Phone until they give a valid answer (waiting for checkPhone)
'''
def getPhone():
    Phone = str(input("Please enter the student Phone \u260E: "))
    if checkPhone(Phone):
        if phoneExists(Phone):
            print("\u274c Student Phone already exists in the system. Please enter a different Phone")
            startPage()
        else:
            return Phone
    else:
        print(f"\u274c Invalid Student Phone")
        getPhone()
'''

#function to ask for a Major until they give a valid answer
def getMajor():
    Major = str(input("Please enter the student Major: "))
    if checkMaj(Major):
        return Major
    else:
        print(f"\u274c Invalid Student Major")
        getMajor()

# The function for if option 5 is selected to display all students
def displayAllPage():
    printPage("StudentRecord.txt")
    displayAll()
    startPage()

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
    startPage()

def modifyStudentPage():
    Id = str(input("Please enter the student ID: "))
    printPage("StudentRecord.txt")
    if checkValID(Id):
        if IDExists(Id):
            displayStudent(Id)
        else:
            print(f"\u274c The student Id {Id} does not exist")
            startPage()
    else:
        print(f"\u274c The student Id {Id} is not valid")
        startPage()

    #waiting for check functions
    '''
    check = True
    while check:
        newName = str(input("New Name: "))
        if newName == "" or checkName(newName):
            check = False
    
    check = True
    while check:
        newPhone = str(input("New Phone: "))
        if newPhone == "" or checkPhone(newPhone):
            check = False
    '''

    check = True
    while check:
        newMajor = str(input("New Major: "))
        if newMajor == "" or checkMaj(newMajor):
            check = False

    #modifyStudent(Id, newName, newPhone, newMajor)