#Function for checking the ID
def checkValID(inp):
    #Check if the length of the ID is valid and that the ID begins with 700
    if(len(inp) == 6 and inp[:3] == "700"):
        return True
    else:
        return False

#Function for checking the name
def checkName(name):
    # While loop to check that there are no digits
    i = 0
    while i < len(name):
        if name[i].isdigit():
            return False
        i += 1

    # Split the name into first and last names
    name_parts = name.split()

    # Check if there are exactly two parts: first name and last name
    if len(name_parts) != 2:
        return False

    first_name, last_name = name_parts

    # Check that both first and last name are at least 2 letters long
    if len(first_name) < 2 or len(last_name) < 2:
        return False

    # Check if the first letter of each name is capitalized and the rest are lowercase
    if not (first_name[0].isupper() and first_name[1:].islower()):
        return False
    if not (last_name[0].isupper() and last_name[1:].islower()):
        return False

    return True

#Function for checking the Phone
def checkPhone(phone):
    # Check that the length is exactly 12 characters
    if len(phone) != 12:
        return False

    # Check if the correct positions contain dashes
    if phone[3] != '-' or phone[7] != '-':
        return False

    # Check if the rest of the characters are digits
    if not (phone[:3].isdigit() and phone[4:7].isdigit() and phone[8:].isdigit()):
        return False

    return True

#Function for checking the Major
def checkMaj(inp):
    #Set made of the Majors in Computer Science
    Majors = ["CS", "CYBR", "SE", "IT", "DS"]
    
    #Check if the Major is valid in the set of majors
    if(inp.upper() in Majors):
        return True
    else:
        return False

#Function for checking if character class is valid
def checkClass(inp):
    #Set made of D&D classes
    Classes = ["BARBARIAN","BARD","CLERIC","DRUID","FIGHTER","MONK","PALADIN","RANGER","ROGUE","SORCERER"
               ,"WARLOCK","WIZARD","ARTIFICER"]
    #Check if input is in the set of Classes
    if(inp.upper() in Classes):
        return True
    else:
        return False

#Function for checking if character level is valid
def checkLevel(inp):
    
    #Check if level is between 1 and 20
    if(1<=inp and inp <= 20):
        return True
    else:
        return False
#Function for checking if character race is valid
def checkRace(inp):
    #Set of D&D races
    Races = ["HUMAN","ARDLING","DRAGONBORN","DWARF","ELF","GNOME","HALFLING","ORC","TIEFLING"]
    
    #Check if input is in Races
    if(inp.upper() in Races):
        return True
    else:
        return False

