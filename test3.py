import json

def main():
    with open('data.json', 'r') as file:
        data = json.load(file)
        print(data)
    print(data[0]["ID"])
    data[0]["ID"] = "700000"
    print(data[0]["ID"])
    with open('data.json', 'w') as file:
        json.dump(data, file)

    check = True
    while check:
        inputFile = open("Welcome.txt", 'r')
        print(inputFile.read())
        choice = input(str("Please Enter the Operation Code: "))
        if (choice == "1"):
            print()
            # addStudent(,)
        elif (choice == "2"):
            print()
        elif (choice == "3"):
            print()
        elif (choice == "4"):
            print()
        elif (choice == "5"):
            print()
        elif (choice == "6"):
            choice2 = str("Are you sure you want to leave (y or n): ")
            if (choice2 == "y"):
                check = False

        else:
            print("Wrong input enter a valid number")

main()