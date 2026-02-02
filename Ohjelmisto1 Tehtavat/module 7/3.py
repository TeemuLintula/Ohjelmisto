airports = {}


def get_airport():
    F_icao = input("Enter the ICAO code: ")
    if F_icao in airports:
        print(f"The airport with ICAO code {F_icao} is {airports[F_icao]}.")
    else:
        print(f"No airport found with ICAO code {F_icao}.")


def new_air():
    N_icao = input("Enter the ICAO code: ")
    A_name = input("Enter the airport name: ")
    airports[N_icao] = A_name
    print(f"Airport {A_name} with ICAO code {N_icao} has been added.")


kysymys = 0
new_airport = ""

while kysymys != 3:
    print("""
Airport Data Management
1. Enter a new airport
2. Fetch airport information
3. Quit""")
    kysymys = int(input("Please choose an option (1-3): "))
    if kysymys == 1:
        new_air()
    elif kysymys == 2:
        get_airport()
    else:
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break