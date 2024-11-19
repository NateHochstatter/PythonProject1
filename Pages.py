from JsonStuff import *
# A file containing functions regarding the pages

# A basic function that prints the requested page
def printPage(filename):
    inputFile = open(filename, 'r')
    print(inputFile.read())
    inputFile.close()

def addStudentPage():
    printPage("AddStudent.txt")
    Id = input("Enter student ID: ")
