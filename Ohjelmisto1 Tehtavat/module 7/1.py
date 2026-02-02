month = int(input("Enter the number of a month (1-12): "))

def get_season(month):
    season = ""
    if month in (12, 1, 2):
        season = "winter"
    elif month in (3, 4, 5):
        season = "spring"
    elif month in (6, 7, 8):
        season = "summer"
    elif month in (9, 10, 11):
        season = "autumn"
    return season

season = get_season(month)
print("You entered:", month)
if season == "":
    print("Please enter a number between 1 and 12.")
else:
    print(f"The season is {season}.")