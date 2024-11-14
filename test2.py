import json
from JsonStuff import *

def main():
    print("Displaying all students")
    displayAll()

    print("Finding individual students")
    displayStudent("700001")
    displayStudent("700003")
    displayStudent("700002")
    displayStudent("700004")

    newData2 = {
        "ID": "700006",
        "Name": "James Bond",
        "Phone": "816-006-6666",
        "Major": "CYBR"}

    addStudent(newData2)

    print("Displaying all students")
    displayAll()


    modifyStudent("700006", "", "James Howler", "816-666-6666", "")

    print("Displaying all students")
    displayAll()

main()