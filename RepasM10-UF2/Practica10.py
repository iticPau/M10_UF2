import random

def entre1y100():
    Num = random.randint(1, 100)
    Intentos = 0
    while True:
        Input = int(input("Escoje un numero entre el 1 y el 100:" ))
        Intentos += 1
        if Input < Num:
            print("Muy pequeño")
        elif Input > Num:
            print("Muy Grande")
        else:
            print(f"Has encontrado el numero {Num} en {Intentos} intentos.")
            break
entre1y100()