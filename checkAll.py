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
