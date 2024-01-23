from Practica28 import numero_aleatorio

def main():
        Num1 = float(input("Escriba un primer numero: "))
        Num2 = float(input("Escriba un segundo numero : "))
        Resultado_aleatorio = numero_aleatorio(Num1, Num2)
        print(f"El numero aleatorio entre {Num1} y {Num2} es: {Resultado_aleatorio}")
if __name__ == "__main__":
    main()
