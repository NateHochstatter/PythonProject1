#Menu that handles deleting students
from JsonStuff import *
import json

def deleteMenu():

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
