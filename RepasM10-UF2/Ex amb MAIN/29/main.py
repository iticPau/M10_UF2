from Practica29 import numeros_y_suma

def main():
    Num1 = int(input("Escriba un primer numero: "))
    Num2 = int(input("Escriba un segundo numero : "))
    suma_enteros = numeros_y_suma(Num1, Num2)
    print(f"La suma de los numeros enteros es: {suma_enteros}")
if __name__ == "__main__":
    main()