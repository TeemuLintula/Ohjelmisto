import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='salasana',
         autocommit=True
         )

cursor = yhteys.cursor()
cursor.execute("select name from airport where iso_country = 'FI';")
tulos = cursor.fetchall()
print(tulos[0])