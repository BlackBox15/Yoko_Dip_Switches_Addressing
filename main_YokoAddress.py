import printDIP
from parseAddressString import parseAddressString

# User input for menu.
# This variable is initialized with "_" (not empty string) because
# in checking for memebership empty string "" will return True in
# any other string (6.10.2. Membership test operations).
menuInput = "_"

#===============================================================================
def printMenu():
    """Print a simple menu."""
    
    print()
    print("1 - set address on DIP")
    print("2 - get address from DIP ")
    print("q - exit")
    print()    

#===============================================================================
def setAddress():
    """Set address on DIP switches from user input."""
    
    MAXDOMAIN = 31
    MAXSTATION = 64
    
    print("Please, input an necessary data:")
    
    try:
        domainNumber = int(input("Domain number (max = 16 for Centum VP, \
max = 31 for ProSafe-RS) --> "))
        stationNumber = int(input("Station number (1-64) --> "))
        
        if domainNumber > MAXDOMAIN \
           or domainNumber < 1 \
           or stationNumber > MAXSTATION \
           or stationNumber < 1:
            raise ValueError

        # Output to console.        
        printDIP.printDIP(domainNumber, stationNumber)
        
    except ValueError:
        print()
        print("Error:")
        print("Input should be an integer in range.")

#===============================================================================
def getAddress():
    """Get address from user input (from DIP switches)."""

    print("""Please input DIP switches configuration \
as string (domain number: 010101101...).""")
    
    domainString = input("DOMAIN --> ")
    stationString = input("STATION --> ")

    address = parseAddressString(domainString, stationString)
    print()
    match(address[0]):
        case 0:
            print("Domain input parameter error.")
        case 1:
            print("Station input parameter error.")
        case 2:
            print("Domain decode error.")
        case 3:
            print("Station decode error.")
        case 4:
            print(f"Domain number: {address[1]}\nStation number: {address[2]}")
    
#====================   Menu cycle  ============================================
while (menuInput not in 'qQ'):
    
    printMenu()
    menuInput = input("--> ")

    try:
        caseNumber = int(menuInput)
    except ValueError:
        continue
    else:
        print()
        match (caseNumber):
            case 1:
                setAddress()
            case 2:
                getAddress()

