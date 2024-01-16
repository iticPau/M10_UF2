def LeerNumeros():
    Numeros = []
    for i in range(10):
        while True:
                num = int(input(f"Escribe el numero {i+1}: "))
                Numeros.append(num)
                break
    return Numeros

def main():
    Numeros = LeerNumeros()
    TupleNum = tuple(Numeros)
    TupleSort = sorted(TupleNum, reverse=True)
    print(f"Numeros ordenados de mayor a menor: {TupleSort}")
if __name__ == "__main__":
    main()