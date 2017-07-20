# Hangman

from hangman_renderer import render_hangman


def convert_upper_case(string):
    if "ß" in string:
        chars = []
        for char in string:
            if char == "ß":
                chars.append("ß")
            else:
                chars.append(char.upper())
        return "".join(chars)
    else:
        return string.upper()


def spielmodus_fragen():
    # Benutzer nach Spielmodus fragen (Einzel/Multi)

    antwort = input("Wählen Sie einen Spielmodus (single/multi): ")
    
    if antwort == "single":
        worte = ["Schmetterling", "Schokokuchen", "Kuhmist", "Faupax", "Rhythmus", "Rhesusfaktor", "Physiognomie", "Jazz", "Fahrradkette", "Steppe", "Militär"]
        import random
        return worte[random.randint(0, len(worte) - 1)]
    else:
        while True:
            eingabe = input("\nGeben Sie das gewünschte Wort ein: ")
            if eingabe.isalpha():
                return eingabe
            else:
                print("\nUngültige Eingabe!")


def zeichne_spiel():
    global falsche_buchstaben, meldung, erratenes_wort, fehlversuche

    print("\n" * 100)

    render_hangman(fehlversuche)

    print("\nFalsche Buchstaben: " + convert_upper_case(", ".join(falsche_buchstaben)) + "\n\n" + meldung + "\n\n" + convert_upper_case(" ".join(erratenes_wort)))


def rate_buchstabe():
    global übrige_buchstaben, meldung
    buchstabe = input("\nRaten Sie einen Buchstaben: ").lower()
    if len(buchstabe) != 1:
        meldung = "Ungültige Eingabe! (Falsche Länge)"
        return False
    elif buchstabe not in list("abcdefghijklmnopqrstuvwxyzäöüß"):
        meldung = "Ungültige Eingabe! (Kein Buchstabe)"
        return False
    elif buchstabe not in übrige_buchstaben:
        meldung = "Ungültige Eingabe! (Bereits versucht)"
        return False
    else:
        return buchstabe


def eingabe_auswerten(buchstabe):
    global fehlversuche, falsche_buchstaben, übrige_buchstaben, meldung, wort, erratenes_wort

    if buchstabe in wort:
        for i in range(len(wort)):
            if wort[i] == buchstabe:
                erratenes_wort[i] = buchstabe
        meldung = "Gut geraten!"
        übrige_buchstaben.remove(buchstabe)
    else:
        fehlversuche += 1
        falsche_buchstaben.append(buchstabe)
        meldung = "Leider falsch geraten!"
        übrige_buchstaben.remove(buchstabe)

    if "_" not in erratenes_wort:
        meldung = "Glückwunsch! Du hast gewonnen."
        return True
    elif fehlversuche == 6:
        meldung = "Zu viele Fehlversuche! Leider verloren."
        return True
    else:
        return False


print("\n" * 100)
print("=== H A N G M A N ===\n\n\n")

while True:

    
    fehlversuche = 0

    falsche_buchstaben = []

    übrige_buchstaben = list("abcdefghijklmnopqrstuvwxyzäöüß")

    meldung = ""

    wort = spielmodus_fragen().lower()

    erratenes_wort = ["_"] * len(wort)
    
    while True:

        zeichne_spiel()

        buchstabe = rate_buchstabe()

        if buchstabe:

            if eingabe_auswerten(buchstabe):
                break
            
    zeichne_spiel()

    print("\n\n")
    
    antwort = input("\nWollen Sie noch einmal? (yes/no) ")
    
    if antwort != "yes":
        break
    else:
        print("\n\n")
