# Programm zur Prüfung des Geburtstages

# Eingaben vom Nutzer erhalten
print("Geben Sie Ihren Geburtstag ein:")
day = int(input("Tag: "))
month = int(input("Monat: "))
year = int(input("Jahr: "))

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
