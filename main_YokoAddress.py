import printDIP
from parseAddressString import parseAddressString

# User input for menu.
# This variable is initialized with "_" (not empty string) because
# in checking for membership empty string "" will return True in
# any other string (6.10.2. Membership test operations).

# menuInput = "_"

MAX_DOMAIN_NUMBER = 31
MAX_STATION_NUMBER = 64


#===============================================================================
def print_menu():
    """Print a simple menu."""
    
    print()
    print("1 - set address on DIP")
    print("2 - get address from DIP ")
    print("q - exit")
    print()    

#===============================================================================
def set_address():
    """Set address on DIP switches from user input."""
    
    print("Please, input an necessary data:")
    
    try:
        domain_number = int(input("Domain number (max = 16 for Centum VP, \
max = 31 for ProSafe-RS) --> "))
        station_number = int(input("Station number (1-64) --> "))
        
        if domain_number > MAX_DOMAIN_NUMBER \
           or domain_number < 1 \
           or station_number > MAX_STATION_NUMBER \
           or station_number < 1:
            raise ValueError

        # Output to console.        
        printDIP.printDIP(domain_number, station_number)
        
    except ValueError:
        print()
        print("Error:")
        print("Input should be an integer in range.")

#===============================================================================
def get_address():
    """Get address from user input (from DIP switches)."""

    print("""Please input DIP switches configuration \
as string (domain number: 010101101...).""")
    
    domain_string = input("DOMAIN --> ")
    station_string = input("STATION --> ")

    address = parseAddressString(domain_string, station_string)
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
def main():
    menu_input = '_'

    while menu_input not in 'qQ':
        print_menu()
        menu_input = input("--> ")

        try:
            case_number = int(menu_input)
        except ValueError:
            continue
        else:
            print()
            match case_number:
                case 1:
                    set_address()
                case 2:
                    get_address()

    print("while doesn't work")

if __name__ == '__main__':
    main()
