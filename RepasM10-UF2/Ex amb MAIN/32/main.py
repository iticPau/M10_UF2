from Practica32 import calcular_cuadrado
def main():
    Lista_numeros = []
    for i in range(10):
        Numero = int(input(f"Ingrese el numero {i + 1}: "))
        Lista_numeros.append(Numero)
    Resultado_cuadrado = calcular_cuadrado(Lista_numeros)
    print(f"Lista de numeros: {Lista_numeros}")
    print(f"Lista de numeros al cuadrado: {Resultado_cuadrado}")
if __name__ == "__main__":
    main()