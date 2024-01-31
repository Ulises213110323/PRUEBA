import random

class JuegoAdivinaNumero:
    def __init__(self, numero_secreto):
        self.numero_secreto = numero_secreto

    def adivinar(self, numero):
        if numero == self.numero_secreto:
            return "¡Felicidades! Has adivinado el número."
        elif numero < self.numero_secreto:
            return "Demasiado bajo. Intenta de nuevo."
        else:
            return "Demasiado alto. Intenta de nuevo."

# Generar un número secreto aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Crear una instancia del juego
juego = JuegoAdivinaNumero(numero_secreto)

print("Bienvenido al juego Adivina el Número.")
print("El objetivo del juego es adivinar un número secreto entre 1 y 100.")
print("Después de cada intento, se te dará una pista si el número es demasiado alto o demasiado bajo.")
print("¡Buena suerte!\n")

# Jugar hasta adivinar el número
while True:
    intento = int(input("Intenta adivinar el número: "))
    resultado = juego.adivinar(intento)
    print(resultado)

    if intento == juego.numero_secreto:
        break