def checkValID(inp):
    if(len(inp) == 6 and inp[:3] == "700"):
        return True
    else:
        return False
def checkMaj(inp):
    Majors = ["CS", "CYBR", "SE", "IT", "DS"]
    if(inp.upper() in Majors):
        return True
    else:
        return False
def checkClass(inp):
    Classes = ["BARBARIAN","BARD","CLERIC","DRUID","FIGHTER","MONK","PALADIN","RANGER","ROGUE","SORCERER"
               ,"WARLOCK","WIZARD","ARTIFICER"]
    if(inp.upper() in Classes):
        return True
    else:
        return False
def checkLevel(inp):
    if(0<inp and inp < 21):
        return True
    else:
        return False
def checkRace(inp):
    Races = ["HUMAN","ARDLING","DRAGONBORN","DWARF","ELF","GNOME","HALFLING","ORC","TIEFLING"]
    if(inp.upper() in Races):
        return True
    else:
        return False

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


def checkName(name):
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