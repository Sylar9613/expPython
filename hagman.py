import random
import os

def run():
    IMAGES = ['''
        +---+
        |   |
            |
            |
            |
            |
      =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
      =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
      =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
      =========''',  '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
      =========''',  '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
      =========''',  '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
      =========''']
    
    DB = [
        "C",
        "HTML",
        "GO",
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "PHP",
        "RUBY",
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 0

    while True:
        os.system("cls")
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[attemps])
        letter = input("Elige una letra\n").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
        
        if not found:
            attemps += 1

        if "_" not in spaces:
            os.system("cls")
            print("Ganaste")
            break
            input()
        
        if attemps == 6:
            os.system("cls")
            print("Perdiste")
            break
            input()


if __name__ == '__main__':
    run()