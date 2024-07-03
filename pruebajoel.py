import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def simulate_typing(word):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    result = ['_'] * len(word)

    for index, target_letter in enumerate(word):
        for letter in alphabet:
            result[index] = letter
            print(''.join(result))
            time.sleep(0.05)  # Ajusta la velocidad de la animación aquí
            if letter == target_letter:
                break
    print(''.join(result))

if __name__ == "__main__":
    word = input("Introduce una palabra: ").lower()
    simulate_typing(word)
