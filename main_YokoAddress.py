import printDIP
from parseAddressString import parse_address_string

# User input for menu.
# This variable is initialized with "_" (not empty string) because
# in checking for membership empty string "" will return True in
# any other string (6.10.2. Membership test operations).

#===============================================================================
def print_menu():
    """Print a menu."""
    
    print()    
    print("--------[ Yoko DIP addressing ]--------")
    print()    
    print("1 set address on DIP")
    print("2 get address from DIP ")
    print("q quit")
    print()    

#===============================================================================
def set_address():
    """Set address on DIP switches from user input."""
    
    maximum_domain_number = 31
    max_station_number = 64
    
    try:
        domain_number = int(input("Domain number (1-31) --> "))
        station_number = int(input("Station number (1-64) --> "))
        
        if domain_number > maximum_domain_number \
           or domain_number < 1 \
           or station_number > max_station_number \
           or station_number < 1:
            raise ValueError

        # Output to console.        
        printDIP.print_dip(domain_number, station_number)
        
    except ValueError:
        print()
        print("Error:")
        print("Input should be an integer in range.")

#===============================================================================
def get_address():
    """Get address from user input (from DIP switches)."""

    print("""Please input DIP switches configuration \
as string (domain number: 10000011...).""")
    
    domain_string = input("DOMAIN --> ")
    station_string = input("STATION --> ")

    address = parse_address_string(domain_string, station_string)
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
            print(f"""\t=========================
        |Domain address:\t{address[1]}
        =========================
        |Station address:\t{address[2]}  
        =========================""")


#====================   Menu cycle  ============================================
while True:
    
    print_menu()
    menuInput = input("--> ")
    print()
    match menuInput:
        case '1':
            print("Set address to DIP.")
            set_address()
        case '2':
            print("Get address from DIP.")
            get_address()
        case 'q' | 'Q':
            print("Program is closing...")
            break
        case _:
            print("\tInput a menu item.")
        

