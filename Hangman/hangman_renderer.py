# Hangman renderer

def render_hangman(fehlversuche):

    if fehlversuche == 1:
        print("               \n               \n               \n               \n               \n               \n               \n               \n===============")
    elif fehlversuche == 2:
        print("               \n            || \n            || \n            || \n            || \n            || \n            || \n            || \n===============")
    elif fehlversuche == 3:
        print("    +=======++ \n            || \n            || \n            || \n            || \n            || \n            || \n            || \n===============")
    elif fehlversuche == 4:
        print("    +=======++ \n         \  || \n          \ || \n           \|| \n            || \n            || \n            || \n            || \n===============")
    elif fehlversuche == 5:
        print("    +=======++ \n    |    \  || \n    |     \ || \n           \|| \n            || \n            || \n            || \n            || \n===============")
    elif fehlversuche == 6:
        print("    +=======++ \n    |    \  || \n    |     \ || \n    0      \|| \n   /|\      || \n   / \      || \n            || \n            || \n===============")

