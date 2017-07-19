jahr = int(input("In welchem Jahr bist du geboren?"))
monat = int(input("In welchem Monat (als Zahl) hast du Geburtstag?"))
tag = int(input("Am wievielten Tag hast du Geburtstag?"))
if tag==19and monat==7:
    print("Herzlichen Glückwunsch")

if (monat == 7 and tag > 19) or monat > 7:
    print("Du bist" ,2016-jahr, "Jahre alt")
else:
    alter=2017-jahr
    print("Du bist" ,alter, "Jahre alt")
    
