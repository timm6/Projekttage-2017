# Multiplikationstafel

while True:

    zahl = int(input("Multiplikationstafel-Generator\n\nGeben Sie die gewünschte Zahl ein: "))

    for i in range(1, 11):
        print(i, "*", zahl, "=", i * zahl)

    antwort = input("\nWollen Sie noch einmal? (yes/no) ")
    
    if antwort != "yes":
        break
    else:
        print("\n\n")
