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

    
    
    # Falls Einzelspieler gewählt wurde folgenden Code ausführen
        worte = ["Schmetterling", "Schokokuchen", "Kuhmist", "Faupax", "Rhythmus", "Rhesusfaktor", "Physiognomie", "Jazz", "Fahrradkette", "Steppe"]
        # hier kannst du noch mehr Wörter einfügen

        import random
        return worte[random.randint(0, len(worte) - 1)]     # diese zwei Zeilen sorgen für die zufällige Auswahl

    # Falls Mehrspieler gewählt wurde folgenden Code ausführen
        # Endlosschleife
            # eigenes Wort vom Spieler erhalten
            # prüfen ob das Wort nur aus Buchstaben besteht: eingabe.isalpha()
                # wenn ja zurückgeben
            # ansonsten
                # Meldung ausgeben, Endlosschleife fortsetzen


def zeichne_spiel():
    global falsche_buchstaben, meldung, erratenes_wort, fehlversuche

    print("\n" * 100)       # 100 leere Zeilen, damit der Bildschirm "leer" ist

    render_hangman(fehlversuche)    # zeichnet den Hangman abhängig der bisherigen Fehlversuche

    # falsche Buchstaben ausgeben
    #
    # convert_upper_case(", ".join(falsche_buchstaben)) erzeugt den auszugebenden Text

    # Meldung ausgeben

    # bisher erratenes Wort ausgeben
    #
    # convert_upper_case(" ".join(erratenes_wort)) erzeugt den auszugebenden Text


def rate_buchstabe():
    global übrige_buchstaben, meldung

    # Buchstabe vom Spieler eingeben lassen, Eingabe in Kleinbuchstaben konvertieren
    
    # wenn die Länge der Eingabe nicht gleich eins ist, False zurückgeben

    # wenn die Eingabe kein Buchstabe ist, False zurückgeben
    #if buchstabe not in list("abcdefghijklmnopqrstuvwxyzäöüß"):
        #return False

    # wenn die Eingabe nicht bei den übrigen Buchstaben ist, False zurückgeben
    #elif buchstabe not in übrige_buchstaben:
        #return False

    # wenn noch nichts zurückgegeben wurde, den eingegebenen Buchstaben zurückgeben

def eingabe_auswerten(buchstabe):
    global fehlversuche, falsche_buchstaben, übrige_buchstaben, meldung, wort, erratenes_wort

    # wenn der Buchstabe im Wort vorkommt
        # jede Stelle des Wortes durchgehen und schauen ob da der eingegebene Buchstabe steht
        # falls ja, dann im erratenen Wort ebendiese Stelle durch den Buchstaben ersetzen
        # Buchstabe von den übrigen Buchstaben entfernen

    # ansonsten
        # Anzahl der Fehlversuche um eins erhöhen
        # Buchstabe zu den falsche Buchstaben hinzufügen
        # Buchstabe von den übrigen Buchstaben entfernen

    # wenn kein "_" mehr im bereits erratenen Wort vorkommt
    #if "_" not in erratenes_wort:
        # Meldung über gewonnenes Spiel setzen
        #return True

    # wenn bereits sechs Fehlversuche gemacht wurden
        # Meldung über Niederlage setzen
        #return True
    
    # wenn noch nichts zurückgegeben wurde, False zurückgeben


print("\n" * 100)
print("=== H A N G M A N ===\n\n\n")

while True:

    
    fehlversuche =          # Anzahl der Fehlversuche auf null setzen

    falsche_buchstaben =    # falsche Buchstaben als leere Liste setzen

    übrige_buchstaben = list("abcdefghijklmnopqrstuvwxyzäöüß")      # erzeugt eine Liste mit allen Buchstaben

    meldung =               # Meldung zu einer leeren Zeichenkette setzen

    wort =                  # Funktion spielmodus_fragen() aufrufen um Wort zu erhalten, Wort in Kleinbuchstaben konvertieren

    erratenes_wort = ["_"] * len(wort)      # erzeugt eine Liste mit so vielen "_" wie das Wort lang ist
    
    while True:

        # Funktion zeichne_spiel() aufrufen

        # Funktion rate_buchstabe() aufrufen um geratenen Buchstaben zu erhalten

        # falls False zurückgegeben wurde, Schleife von vorne beginnen (continue)

        # andernfalls eingabe_auswerten(buchstabe) aufrufen

        # falls dies True zurückgibt, Schleife abbrechen (break)
            
    # am Ende des Spiels noch einmal neu zeichnen mit der Funktion zeichne_spiel()

    print("\n\n")
    
    antwort = input("\nWollen Sie noch einmal? (yes/no) ")
    
    if antwort != "yes":
        break
    else:
        print("\n\n")
