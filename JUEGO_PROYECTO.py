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
        
    def obtener_nombre_usuario():
        nombre = input ("Hola! Cual es tu nombre?")
        return nombre
    
    nombre_usuario = obtener_nombre_usuario()
    print(f"Hola {nombre_usuario}, vamos a jugar a adivinar el número XD")


numero_secreto = random.randint(1, 100)


juego = JuegoAdivinaNumero(numero_secreto)


while True:
    intento = int(input("Intenta adivinar el número: "))
    resultado = juego.adivinar(intento)
    print(resultado)

    if intento == juego.numero_secreto:
        break