import random

class JuegoAdivinaNumero:
    def __init__(self, numero_secreto):
        self.numero_secreto = numero_secreto

    def adivinar(self, numero):
        if numero == self.numero_secreto:
            return "\033[92m¡Felicidades! Has adivinado el número.\033[0m"
        elif numero < self.numero_secreto:
            return "\033[91mDemasiado bajo. Intenta de nuevo.\033[0m"
        else:
            return "\033[91mDemasiado alto. Intenta de nuevo.\033[0m"
        
nombre_usuario = input("Hola! Cual es tu nombre?")

while True:
    dificultad = input("Elige la dificultad (facil/dificil): ").lower()
    if dificultad in ['facil', 'dificil']:
        break
    else:
        print("Por favor, ingresa 'facil' o 'dificil'.")

while True:
    numero_secreto = random.randint(1, 100)
    juego = JuegoAdivinaNumero(numero_secreto)
    intentos_maximos = 10 
    intentos_realizados = 0 

    while intentos_realizados < intentos_maximos:
        intento = int(input("Intenta adivinar el número: "))
        resultado = juego.adivinar(intento)
        print(resultado)

        intentos_realizados += 1

        if intento == juego.numero_secreto:
            print(f"¡Adivinaste el número en {intentos_realizados} intentos!")
            break

    if intento != juego.numero_secreto:
        print(f"Has alcanzado el límite de {intentos_maximos} intentos. ¡Perdiste! El número secreto era {juego.numero_secreto}.")

    
    jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_nuevamente != 's':
        print(f"¡Gracias por jugar, {nombre_usuario} o⁠(⁠(⁠^⁠▽⁠ ^⁠⁠)⁠)⁠o!!")
        break
