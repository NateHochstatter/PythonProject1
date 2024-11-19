import json

#Function to add a new student
def addStudent(newStudent, filename="data.json"):
    with open(filename, 'r') as file:
        data = json.load(file)
        data.append(newStudent)

    with open(filename, 'w') as file:
        json.dump(data, file)

#Function to delete a student
def deleteStudent(ID, filename="data.json"):
    with open(filename, 'r') as file:
        data = json.load(file)

    count = 0
    for student in data:
        if student["ID"] == ID:
            del data[count]
            break
        else:
            count += 1

    with open(filename, 'w') as file:
        json.dump(data, file)

#Function to find the index of the student with the given id
def findStudent(ID, filename="data.json"):
    count = 0
    with open(filename, 'r') as file:
        data = json.load(file)
        for student in data:
            if student["ID"] == ID:
                return count
            else:
                count += 1

#Function to display the student with a given id
def displayStudent(ID, filename="data.json"):
    index = findStudent(ID)
    with open('data.json', 'r') as file:
        data = json.load(file)
    print("Id: " + str(data[index]["ID"]) + " Name: " + str(data[index]["Name"]) + " Phone "
          + str(data[index]["Phone"]) + " Major " + str(data[index]["Major"]))

#Function to display all students in the file
def displayAll(filename="data.json"):
    with open(filename, 'r') as file:
        data = json.load(file)
        for student in data:
            print("Id: " + str(student["ID"]) + " Name: " + str(student["Name"]) + " Phone "
                  + str(student["Phone"]) + " Major " + str(student["Major"]))

#Function to modify a students data
def modifyStudent(oldID, newID, newName, newPhone, newMajor, filename="data.json"):
    index = findStudent(oldID)
    with open('data.json', 'r') as file:
        data = json.load(file)
    if newID != "":
        data[index]["ID"] = newID
    if newName != "":
        data[index]["Name"] = newName
    if newPhone != "":
        data[index]["Phone"] = newPhone
    if newMajor != "":
        data[index]["Major"] = newMajor
    with open(filename, 'w') as file:
        json.dump(data, file)

#Function to find if the id given already exists
def IDExists(ID, filename="data.json"):
    with open(filename, 'r') as file:
        data = json.load(file)
        for student in data:
            if student["ID"] == ID:
                return True
    return False
