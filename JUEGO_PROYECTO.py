import random

class JuegoAdivinaNumero:
    def __init__(self, numero_secreto):
        self.numero_secreto = numero_secreto

    def adivinar(self, numero):
        if numero == self.numero_secreto:
            return True, "¡Felicidades! Has adivinado el número."
        elif numero < self.numero_secreto:
            return False, "Demasiado bajo. Intenta de nuevo."
        else:
            return False, "Demasiado alto. Intenta de nuevo."

while True:
    dificultad = input("Elige la dificultad (facil/dificil): ").lower()
    if dificultad in ['facil', 'dificil']:
        break
    else:
        print("Por favor, ingresa 'facil' o 'dificil'.")

while True:
    # Generar un número secreto aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)

    # Crear una instancia del juego
    juego = JuegoAdivinaNumero(numero_secreto)

    # Jugar hasta adivinar el número
    while True:
        intento = int(input("Intenta adivinar el número: "))
        resultado, mensaje = juego.adivinar(intento)
        print(mensaje)

        if resultado:
            jugar_nuevamente = input("¡Felicidades! ¿Quieres jugar de nuevo? (s/n): ").lower()
            if jugar_nuevamente != 's':
                print("¡Gracias por jugar!")
                break
            else:
                break