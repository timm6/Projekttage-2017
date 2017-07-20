# Hangman

fehlversuche = 0

falsche_buchstaben = []

meldung = ""

wort = ""

erratenes_wort = []

def spielmodus_fragen():
    # ausgeben/eingeben
    return None


def zeichne_spiel():
    global falsche_buchstaben, meldung

    # zeichne Hangman -> Alex schreiben

    print(falsche_buchstaben.join(", "))
    print(meldung)
    print(erratenes_wort.join(" "))


def rate_buchstabe():
    pass

    

while True:

    wort = spielmodus_fragen()
    
    while True:

        zeichne_spiel()

        buchstabe = rate_buchstabe()
        

    
    antwort = input("\nWollen Sie noch einmal? (yes/no) ")
    
    if antwort != "yes":
        break
    else:
        print("\n\n")
