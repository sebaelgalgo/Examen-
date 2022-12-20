import os
import random

secreto = random.randint(1, 100)
usuario = -1
while usuario != secreto:
    os.system ('cls')
    usuario = int(input("¿Cuál es el Número "))
    if usuario < secreto:
        print("Tu número es menor")
    elif usuario > secreto:
        print("Tu número es mayor")
    else:
        print("Has acertado")
    input ("Si presionas ENTER Vuelves a intentarlo ")
        