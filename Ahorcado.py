import random

# Etapas del ahorcado (dibujos en ASCII)
AHORCADO = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Lista de palabras para el juego
palabras = ["python", "programacion", "ahorcado", "inteligencia", "robot", "algoritmo", "computadora"]

# Elegir palabra al azar
palabra = random.choice(palabras).lower()
letras_adivinadas = []
intentos = len(AHORCADO) - 1

print("¡Bienvenido al juego del Ahorcado!")
print(AHORCADO[0])

while intentos > 0:
    # Mostrar progreso
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    print("\nPalabra:", progreso)

    # Verificar victoria
    if "_" not in progreso:
        print(f"🎉 ¡Ganaste! La palabra era: {palabra}")
        break

    # Pedir letra hasta que sea válida (una sola letra)
    letra = ""
    while True:
        letra = input("Adivina una letra: ").lower().strip()
        if len(letra) == 1 and letra.isalpha():
            break
        else:
            print("⚠️ Solo puedes ingresar una **letra** (no números ni varias letras).")

    # Verificar si ya fue usada
    if letra in letras_adivinadas:
        print("⚠️ Ya intentaste esa letra.")
        continue

    letras_adivinadas.append(letra)

    # Verificar si la letra está en la palabra
    if letra in palabra:
        print("✅ ¡Bien hecho! La letra está en la palabra.")
    else:
        intentos -= 1
        print("❌ Letra incorrecta.")
        print(AHORCADO[len(AHORCADO) - 1 - intentos])
        print(f"Te quedan {intentos} intentos.")

# Si pierde
if intentos == 0:
    print(f"💀 Perdiste. La palabra era: {palabra}")
