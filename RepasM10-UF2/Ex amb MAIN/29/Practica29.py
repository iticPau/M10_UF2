def numeros_y_suma(Num1, Num2):
    if Num1 > Num2:
        Num1, Num2 = Num2, Num1 
    Numeros_enteros = list(range(int(Num1), int(Num2) + 1))
    Suma_enteros = sum(Numeros_enteros)

    print(f"Numeros enteros entre {Num1} y {Num2}: {Numeros_enteros}")

    return Numeros_enteros, Suma_enteros