from Pages import *
def start():
    printPage("Welcome.txt")
    choice = input(str("Please Enter the Operation Code: "))
    
    ex = False
    if(ex!= True):
        while(choice != "6"):
            if(choice == "1"):
                print()
                addStudentPage()
            elif(choice == "2"):
                print() 
            elif(choice == "3"):
                print() 
            elif(choice == "4"):
                print() 
            elif(choice == "5"):
                print() 
            else:
                print("Wrong input enter a valid number")
            inputFile = open("Welcome.txt",'r')
            print(inputFile.read())
            choice = input(str("Please Enter the Operation Code: "))
        leave = input(str("Do you want to Exit the System? Enter Y to Confirm: "))
        if(leave == "Y"):
            ex = True

            

    
start()
