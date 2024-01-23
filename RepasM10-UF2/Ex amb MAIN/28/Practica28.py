import random

def numero_aleatorio(Num1, Num2):
    if Num1 > Num2:
        Num1, Num2 = Num2, Num1  
    Numero_aleatorio = random.uniform(Num1, Num2)
    return Numero_aleatorio