import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", 
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número de fallos permitidos
failures = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
while True:
    difficulty = input("¿Con qué nivel de dificultad deseas jugar? (1)Fácil (2)Media (3)Difícil ")
    if difficulty.isdigit():
        difficulty = int(difficulty)
        if 1 <= difficulty <= 3:
            break
        print("No has elegido una de las opciones. Reintentalo.")
    else:
        print("No has elegido una de las opciones. Reintentalo.")
# Verifica qué nivel de dificultad fué elegido
match difficulty:
    case 1:
        vowels = ["a", "e", "i", "o", "ó", "u"]
        word = []
        for letter in secret_word:
            if letter in vowels:
                word.append(letter)
                guessed_letters.append(letter)
            else:
                word.append("_") 
        word_displayed = "".join(word)
    case 2:
        word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
    case 3:
        word_displayed = "_" * len(secret_word)
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
while failures:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    # Verificar si el valor de la letra es un string vacío ""
    if not letter:
        print("No has ingresado ninguna letra.")
        continue
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        failures -= 1
    # Mostrar la palabra parcialmente adivinada
    letters = []
    match difficulty:
        case 2:
            letters.append(secret_word[0])
            for letter in secret_word[1:-1]:
                if letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
            letters.append(secret_word[-1])
        case _:
            for letter in secret_word:
                if letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print("¡Oh no! Has alcanzado el máximo de fallos permitidos.")
    print(f"La palabra secreta era: {secret_word}")