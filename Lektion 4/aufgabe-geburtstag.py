# Programm zur Prüfung des Geburtstages

monate = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]

while True:

    # Eingaben vom Nutzer erhalten
    print("Geben Sie Ihren Geburtstag ein:")
    day = int(input("Tag: "))
    month = input("Monat (als Wort): ")
    year = int(input("Jahr: "))

    month = monate.index(month) + 1

    if month < 7 or (month == 7 and day < 19):    # vor Juli oder vor dem 19. Juli
        print("Sie hatten dieses Jahr bereits Geburtstag.")
    elif month == 7 and day == 19:                 # genau am 19. Juli
        print("HERZLICHEN GLÜCKWUNSCH!")
        print("Sie haben heute Geburtstag!")
    else:                                           # nach dem 19. Juli bleibt übrig
        print("Sie hatten dieses Jahr noch nicht Geburtstag.")

    if month < 7 or (month == 7 and day <= 19):   # vor Juli oder vor oder am 19. Juli
        print("Sie sind", 2017 - year, "Jahre alt.")
    else:                                           # nach dem 19. Juli
        print("Sie sind", 2016 - year, "Jahre alt.")

    antwort = input("\nWollen Sie noch einmal? (yes/no) ")
    
    if antwort != "yes":
        break
    else:
        print("\n\n")
