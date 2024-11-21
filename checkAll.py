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
    Classes = ["Barbarian","Bard","Cleric","Druid","FIghter","Monk","Paladin","Ranger","Rogue","Sorcerer"
               ,"Warlock","Wizard","Artificer"]
    if(inp in Classes):
        return True
    else:
        return False
    
