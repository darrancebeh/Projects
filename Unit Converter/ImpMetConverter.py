import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    option = int(input("1 - Weight\n2 - Temperature\n3 - Length\n\n"))
    if option == 1:
        weight()
    elif option == 2:
        temperature()
    elif option == 3:
        length()
    else:
        main()

def weight():
    clear()
    print("CATEGORY: WEIGHT\n")
    option2 = int(input("1 - Pound, lb -> Kilogram, kg\n2 - Kilogram, kg -> Pound, lb\n3 - Return to Main Menu.\n\n"))

    if option2 == 1:
        clear()
        pound = int(input("Input value, in lb: "))
        print("\nInput value: " + str(pound) + " lb.")
        kg = pound * 0.45359237
        print("Returned value: " + str(kg) + " kg." )

    elif option2 == 2:
        clear()
        kg = int(input("Input value, in kg: "))
        print("\nInput value: " + str(kg) + " kg.")
        pound = kg * 2.20462
        print("Returned value: " + str(pound) + " lb.")

    elif option2 == 3:
        main()
    
    else:
        weight()

def temperature():
    clear()
    print("CATEGORY: TEMPERATURE\n")
    option2 = int(input("1 - Fahrenheit, °F -> Celsius, °C\n2 - Celsius, °C -> Fahrenheit, °F\n3 - Return to Main Menu.\n\n"))

    if option2 == 1:
        clear()
        fahren = int(input("Input value, in °F: "))
        print("\nInput value: " + str(fahren) + " °F.")
        celsius = (fahren - 32) * 5/9
        print("Returned value: " + str(celsius) + " °C.")

    elif option2 == 2:
        clear()
        celsius = int(input("Input value, in °C: "))
        print("\nInput value: " + str(celsius) + " °C.")
        fahren = (celsius * 9/5) + 32
        print("Returned value: " + str(fahren) + " °F.")

    elif option2 == 3:
        main()

    else:
        temperature()

def length():
    clear()
    print("CATEGORY: LENGTH\n")
    option2 = int(input("1 - Mile, mi -> Kilometre, km\n2 - Kilometre, km -> Mile, mi\n3 - Return to Main Menu.\n\n"))

    if option2 == 1:
        clear()
        mile = int(input("Input value, in mi: "))
        print("\nInput value: " + str(mile) + " mi.")
        km = mile * 1.609344
        km = round(km, 4)
        print("Returned value: " + str(km) + " km.")

    elif option2 == 2:
        clear()
        km = int(input("Input value, in km: "))
        print("\nInput value: " + str(km) + " km.")
        mile = km / 1.609344
        mile = round(mile, 4)
        print("Returned value: " + str(mile) + " mi.")

    elif option2 == 3:
        main()
    
    else:
        length()

def control():
    main()
    while input("\n_________________________________________________\n\nWould you like to return to the main menu? (Y/N)\n").lower()[0] == 'y':
        main()
    clear()
    input("Thank you for using darrance's unit converter!\n")

control()
