def main():
    Num_usuario = input("Introduce 10 numeros separados por espacios: ")
    Llista_num = [int(numero) for numero in Num_usuario.split()]
    Suma = sum(Llista_num)
    Media = Suma / len(Llista_num)
    Llista_num.append(f"Numeros del usuario: {Num_usuario}")
    Llista_num.append(f"Suma total: {Suma}")
    Llista_num.append(f"Media: {Media}")
    print("Lista final:")
    for elemento in Llista_num:
        print(elemento)
if __name__ == "__main__":
    main()
