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

