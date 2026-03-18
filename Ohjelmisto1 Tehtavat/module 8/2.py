import mysql.connector

def findAirport(code):

    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='salasana',
        autocommit=True
    )

    cursor = yhteys.cursor()
    cursor.execute(f"select type from airport where iso_country = '{code}'")

    tulos = cursor.fetchall()
    if not tulos:
        return None
    else:
        return tulos

#Pääohjelma
CountryCode = input("Enter the country code (e.g., FI for Finland): ").upper()
airports = findAirport(CountryCode)

small = 0
large = 0
medium = 0
heliport = 0

if airports is None:
    print("No airport found for country code", CountryCode)
else:
    for airport in airports:
        if airport[0] == "small_airport":
            small += 1
        elif airport[0] == "large_airport":
            large += 1
        elif airport[0] == "medium_airport":
            medium += 1
        elif airport[0] == "heliport":
            heliport += 1
    print("Airports in", CountryCode + ":")
    print(str(small), "small_airports")
    print(str(medium), "medium_airports")
    print(str(heliport), "heliport_airports")
    print(str(large), "large_airports")
