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
                print()
                addStudentPage()
            elif (choice == "2"):
                print()
            elif (choice == "3"):
                print()
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


def getId():
    Id = input("Please enter the student ID: ")
    if checkValID(Id):
        Name = input("Please enter the student name (Firstname Lastname): ")

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


