import json

#Function to add a new student
def addStudent(newStudent, filename="data.json"):
    with open(filename, 'r') as file:
        data = json.load(file) #Gets the info from the json
        data.append(newStudent) #Adds the new students data to the json info

    with open(filename, 'w') as file:
        json.dump(data, file) #Writes the new json info with the new student to the file

#Function to find the index of the student with the given id
def findStudent(ID, filename="data.json"):
    count = 0 #Made a count variable
    with open(filename, 'r') as file:
        data = json.load(file) #Gets the info from the file and loops trough each student
        for student in data:
            if student["ID"] == ID: #Checks if the students ID is the one being looked for
                #If it is return the count to act as an index otherwise increase count
                return count
            else:
                count += 1

#Function to display the student with a given id
def displayStudent(ID, filename="data.json"):
    index = findStudent(ID) #Call the findStudent function to get the index of the student
    with open('data.json', 'r') as file:
        data = json.load(file) #Gets the info from the json
    #Print the info of the selected student in an organized manner
    print("Id: " + str(data[index]["ID"]) + " Name: " + str(data[index]["Name"]) + " Phone "
          + str(data[index]["Phone"]) + " Major " + str(data[index]["Major"]))

#Function to display all students in the file
def displayAll(filename="data.json"):
    #Note all prints for this function are formated for consistent look
    print(f"{'ID':<8} {'Name':<15} {'Phone':<15} {'Major':<5}") #Print header for the table
    with open(filename, 'r') as file:
        data = json.load(file) #Gets the info from the file and loops trough each student
        for student in data:
            # Print the info of each student as it loops through them
            print(f"{str(student["ID"]):<8} {str(student["Name"]):<15} "
                  f"{(str(student["Phone"])):<15} {(str(student["Major"])):<5}")

#Function to modify a students data
def modifyStudent(oldID, newName, newPhone, newMajor, filename="data.json"):
    index = findStudent(oldID) #Call the findStudent function to get the index of the student
    with open('data.json', 'r') as file:
        data = json.load(file) #Gets the info from the json
    #A series of if statements to check if they wanted to modify the element being checked
    #If a new element was provided then it sets the old element of the student at the index to the new one
    if newName != "":
        data[index]["Name"] = newName
    if newPhone != "":
        data[index]["Phone"] = newPhone
    if newMajor != "":
        data[index]["Major"] = newMajor
    with open(filename, 'w') as file:
        json.dump(data, file) #Writes the updated student info to the json

#Function to find if the id given already exists
def IDExists(ID, filename="data.json"):
    with open(filename, 'r') as file:
        data = json.load(file) #Gets the info from the file and loops trough each student
        for student in data:
            if student["ID"] == ID: #Checks if the student's ID matches the provided ID
                #If so return true to indicate that the ID already exists
                return True
    return False #Return false if n student has the ID

#Function to find if the Name given already exists
def NameExists(Name, filename="data.json"):
    with open(filename, 'r') as file:
        data = json.load(file) #Gets the info from the file and loops trough each student
        for student in data:
            if student["Name"] == Name: #Checks if the student's Name matches the provided Name
                #If so return true to indicate that the Name already exists
                return True
    return False

#Function to find if the Phone given already exists
def PhoneExists(Phone, filename="data.json"):
    with open(filename, 'r') as file:
        data = json.load(file) #Gets the info from the file and loops trough each student
        for student in data:
            if student["Phone"] == Phone: #Checks if the student's Phone matches the provided Phone
                #If so return true to indicate that the Phone already exists
                return True
    return False