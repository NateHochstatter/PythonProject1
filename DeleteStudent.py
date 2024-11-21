from JsonStuff import *
import json

def deleteMenu():

    #Prompt the user to enter a student ID to delete
    IDInput = input("Please enter a Student ID to delete: ")
    if IDExists(IDInput) == True:
        print("=====Student Record=====")
        displayStudent(IDInput)

        #Iterate the verification question until the user responds with Y or N
        validResponse = False
        while(validResponse == False):
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
    else:
        print("Student ID does not exist")

deleteMenu()
