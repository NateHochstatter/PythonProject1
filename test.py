import json
from JsonStuff import *

def main():
    data = [
        {"ID": "700001",
         "Name": "Emily White",
         "Phone": "816-111-1111",
         "Major": "CS"},
        {"ID": "700002",
         "Name": "David Bachman",
         "Phone": "816-222-2222",
         "Major": "CYBR"},
        {"ID": "700003",
         "Name": "Jason James",
         "Phone": "816-333-3333",
         "Major": "SE"}
    ]

    # Convert to JSON string
    json_string = json.dumps(data,indent=4)
    print(json_string)

    # Write to a file
    with open('data.json', 'w') as file:
        json.dump(data, file)

    with open('data.json', 'r') as file:
        data = json.load(file)
        print(data)

    for student in data:
        print(student["ID"])

    newData = {
        "ID": "700004",
        "Name": "Nate Stars",
        "Phone": "816-444-4444",
        "Major": "CS"}

    with open('data.json', 'r') as file:
        data = json.load(file)
        data.append(newData)
        print(data)

    with open('data.json', 'w') as file:
        json.dump(data, file)

    print(findStudent("700001"))

    newData2 = {
        "ID": "700005",
        "Name": "Bob Builder",
        "Phone": "816-555-5555",
        "Major": "SE"}

    addStudent(newData2)

    print("Another student added")

    with open('data.json', 'r') as file:
        data = json.load(file)
        print(data)



main()