def main():
    Frase = input("Escribe una frase: ")
    Frase_sin_espacios = Frase.replace(" ", "")
    TupleFrase = (Frase_sin_espacios)
    print("Frase sin espacios: ", TupleFrase)
if __name__ == "__main__":
    main()