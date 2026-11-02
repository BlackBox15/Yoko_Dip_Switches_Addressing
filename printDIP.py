from convertIntToBoolArray import int_to_bool_array

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
    
def print_dip(domain_number, station_number):
    """Вывод внешнего вида DIP-переключателей"""

    dipSwitchesStringView = []
    
    ## Формирование массива boolean-значений.
    stationSwitches = int_to_bool_array(station_number)
    domainSwitches = int_to_bool_array(domain_number)
    
    dipSwitchesStringView.extend(convertToStrig(domainSwitches))
    dipSwitchesStringView.extend(convertToStrig(stationSwitches))
    
    print()
    print(f"""	==========================
	|Domain address:\t{domain_number}
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
	|Station address:\t{station_number}  
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

