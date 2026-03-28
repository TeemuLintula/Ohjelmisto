import requests

try:
    vastaus = requests.get("https://api.chucknorris.io/jokes/random")
    if vastaus.status_code == 200:
        vastaus = vastaus.json()
        print(vastaus["value"])
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")