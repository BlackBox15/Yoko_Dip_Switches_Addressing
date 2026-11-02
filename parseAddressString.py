def parse_address_string(domain_string, station_string):
    """Parsing input strings to Domain and Station addresses."""

    domainNameInList = []
    stationNameInList = []
    result = []

    ## Errors code
    DOMPARERROR = 0
    STNPARERROR = 1
    DOMDECODEERROR = 2
    STNDECODEERROR = 3
    NORMAL = 4
    
    # Checking the length of input string (domain number).
    # Domain address - strictly 8 symbols.
    # 1, 2 bit strictly equal 0.
    
    if len(domain_string) == 8 and \
            domain_string[1] == '0' and \
            domain_string[2] == '0':
        
        domainNameInList = pack_string_to_integer(domain_string)
        
    else:
        result.insert(0, DOMPARERROR)
        return result
    
    # Checking the length of input string (station number).
    # Station address - strictly 8 symbols.
    
    if len(station_string) == 8:
        
        stationNameInList = pack_string_to_integer(station_string)
        
    else:
        result.insert(0, STNPARERROR)
        return result

    ## Parity bits.
    domainParityBit = domainNameInList[0]
    stationParityBit = stationNameInList[0]

    ## Quantity of "1"s in addressing area.
    domainQnttyBits = domainNameInList[3:].count(1)
    stationQnttyBits = stationNameInList[1:].count(1)

    if (domainQnttyBits % 2 == 0 and domainParityBit == 1) or \
       (domainQnttyBits % 2 != 0 and domainParityBit == 0):
        
        domainAddress = get_address_number(domainNameInList[3:])
        result.insert(1, domainAddress)

        
    else:
        result.insert(0, DOMDECODEERROR)
        return result
        
    if (stationQnttyBits % 2 == 0 and stationParityBit == 1) or \
       (stationQnttyBits % 2 != 0 and stationParityBit == 0):
        
        stationAddress = get_address_number(stationNameInList[1:])
        result.insert(2, stationAddress)
        
    else:
        result.insert(0, STNDECODEERROR)
        return result

        result.insert(0, NORMAL)
    result.insert(0, NORMAL)
    return result
## ================================================================
def get_address_number(input_integer):
    """Convert Binary List to Integer"""

    result = 0
    powerOfTwo = len(input_integer) - 1

    for number in input_integer:
        if number == 1:
            
            result += 1 * pow(2, powerOfTwo)
            
        powerOfTwo -= 1

    return result
## ================================================================
def pack_string_to_integer(input_string):
    """String \"010101011010\" to Integer array [0,1,0,1,0...]"""

    ## Empty Integer list.
    result = []
    
    for single_symbol in input_string:
        match single_symbol:
            case("0"):
                result.append(0)
            case("1"):
                result.append(1)

    return result
