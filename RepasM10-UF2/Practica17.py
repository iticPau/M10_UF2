def main():
    Frase = input("Escribe una frase: ")
    Frase_sin_repetidos = "".join(sorted(set(Frase), key=Frase.index))
    TupleFrase = (Frase_sin_repetidos)
    print(f"Frase sin caracteres repetidos: {TupleFrase}")
if __name__ == "__main__":
    main()
