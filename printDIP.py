from convertIntToBoolArray import intToBoolArray 

def convertToStrig(booleanList):
    """Conversation from boolean list to special string list."""
    
    stringOfFalse = "  *   |      "
    stringOfTrue = "      |   *  "
    result = []
    
    for k in range(0, len(booleanList)):
        if booleanList[k] == True:
            result.append(stringOfTrue)
        else:
            result.append(stringOfFalse)

    return result
    
def printDIP(domainNumber, stationNumber):
    """Вывод внешнего вида DIP-переключателей"""

    dipSwitchesStringView = []
    
    ## Формирование массива boolean-значений.
    stationSwitches = intToBoolArray(stationNumber)
    domainSwitches = intToBoolArray(domainNumber)
    
    dipSwitchesStringView.extend(convertToStrig(domainSwitches))
    dipSwitchesStringView.extend(convertToStrig(stationSwitches))
    
    print()
    print(f"""	==========================
	|Domain address:\t{domainNumber}
	==========================
	|  off  |  on  |
	----------------------
	1|{dipSwitchesStringView[0]}|parity
	2|{dipSwitchesStringView[1]}|off
	3|{dipSwitchesStringView[2]}|off
	4|{dipSwitchesStringView[3]}|16
	5|{dipSwitchesStringView[4]}|8
	6|{dipSwitchesStringView[5]}|4
	7|{dipSwitchesStringView[6]}|2
	8|{dipSwitchesStringView[7]}|1
	==========================
	|Station address:\t{stationNumber}  
	==========================
	|  off  |  on  |
	----------------------
	1|{dipSwitchesStringView[8]}|parity
	2|{dipSwitchesStringView[9]}|64
	3|{dipSwitchesStringView[10]}|32
	4|{dipSwitchesStringView[11]}|16
	5|{dipSwitchesStringView[12]}|8
	6|{dipSwitchesStringView[13]}|4
	7|{dipSwitchesStringView[14]}|2
	8|{dipSwitchesStringView[15]}|1
	======================

""")

