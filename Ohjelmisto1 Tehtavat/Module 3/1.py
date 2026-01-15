zander_lenght = float(input("Enter the length of the zander in centimeters: "))
if zander_lenght < 42:
    puuttuvat_sentit = float(42 - zander_lenght)
    print("The zander does not meet the size limit.\nPlease release the fish back into the lake.")
    print(f"The fish was {puuttuvat_sentit:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")