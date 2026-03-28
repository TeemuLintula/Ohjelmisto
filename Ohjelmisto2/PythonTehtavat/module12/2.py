import requests

kunta = input("Enter municipality name: ")
API = "9da07571197c948ef002a4263c0d841a"
pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={kunta}&appid={API}&units=metric&lang=fi"

try:
    vastaus = requests.get(pyynto)

    if vastaus.status_code == 200:
        data = vastaus.json()

        print(f"Kaupunki: {data['name']}")
        print(f"Sää: {data['weather'][0]['description']}")
        print(f"Lämpötila: {data['main']['temp']} °C")

    else:
        print("Virhe, status code:", vastaus.status_code)

except requests.exceptions.RequestException as e:
    print("Virhe pyynnössä:", e)