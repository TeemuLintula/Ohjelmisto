import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='salasana',
         autocommit=True
         )

def findAirport(ICAO):
    cursor = yhteys.cursor()
    cursor.execute(f"select name, municipality from airport where ident = '{ICAO}'")
    tulos = cursor.fetchone()
    if tulos is None:
        return None
    else:
        return tulos

#Pääohjelma
ICAO = input("Enter the ICAO code of an Airport: ").upper()
airport = findAirport(ICAO)
if airport is None:
    print("No airport found with ICAO code", ICAO)
else:
    print("Airport name:", airport[0])
    print("Location:", airport[1])