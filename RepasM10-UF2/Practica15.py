def LeerNumeros():
    Numeros = []
    while True:
        num = int(input("Escribe un numero: "))
        if num == 0:
            break
        Numeros.append(num)
    return Numeros

def main():
    Numeros = LeerNumeros()
    TupleNum = tuple(Numeros)
    if TupleNum:
        TupleSort = sorted(TupleNum, reverse=True)
        print(f"Numeros ordenados de mayor a menor: {TupleSort}")
if __name__ == "__main__":
    main()
