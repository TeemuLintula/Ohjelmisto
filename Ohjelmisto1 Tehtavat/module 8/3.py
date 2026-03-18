import mysql.connector
import geopy
from geopy.distance import distance

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
    cursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{ICAO}'")
    tulos = cursor.fetchone()
    if tulos is None:
        return None
    else:
        return tulos

#Pääohjelma
ICAO1 = input("Enter the ICAO code of the first Airport: ").upper()
ICAO2 = input("Enter the ICAO code of the second Airport: ").upper()

airport1 = findAirport(ICAO1)
airport2 = findAirport(ICAO2)

if airport1 is None or airport2 is None:
    print("No airport found with ICAO code", ICAO1, "or", ICAO2)
else:
    print(f"Distance between {ICAO1} and {ICAO2}: {distance((airport1[0], airport1[1]), (airport2[0], airport2[1])).kilometers} kilometers")
