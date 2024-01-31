import random

class JuegoAdivinaNumero:
    def __init__(self, numero_secreto):
        self.numero_secreto = numero_secreto

    def adivinar(self, numero):
        if numero == self.numero_secreto:
            return  "\033[92m¡Felicidades! Has adivinado el número.\033[0m"
        elif numero < self.numero_secreto:
            return "\033[91mDemasiado bajo. Intenta de nuevo.\033[0m"
        else:
            return "\033[91mDemasiado alto. Intenta de nuevo.\033[0m"
        

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
    
if intentos_realizados == intentos_maximos:
    print(f"Has alcanzado el límite de {intentos_maximos} intentos. ¡Perdiste! El número secreto era {juego.numero_secreto}.")