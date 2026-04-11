from flask import Flask
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='salasana',
         autocommit=True
         )
app = Flask(__name__)

@app.route('/kentta/<string:icao>', methods=['GET'])

def tarkista_alkuluku(icao):
    cursor = yhteys.cursor()
    cursor.execute(f"select ident, name, municipality from airport where ident = '{icao}'")
    tulos = cursor.fetchall()
    tulos = {
        "ICAO" : tulos[0][0],
        "Name" : tulos[0][1],
        "Municipality" : tulos[0][2]
    }

    return tulos

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)

