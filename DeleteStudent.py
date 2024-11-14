import json

#Method to delete students
def deleteStudent():

    #Prompt the user to enter a user ID to delete
    deleteID = int(input("Please enter the student ID you want to delete: "))

    canDelete = IDExists(deleteID, '''insert json file here''')

    #If canDelete is true, delete the ID
    if canDelete:
        with open("data.json","r") as file:
        data.json = json.load(file)
        if deleteID in data:
            del data[deleteID]
            #This needs changed so it deletes all of the information instead
            #of just the ID
            #Also the method is just not finished yet

    

    
