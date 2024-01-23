from Practica27 import suma_dos_numeros

def main():
    Num1 = float(input("Escriba un primer numero: "))
    Num2 = float(input("Escriba un segundo numero: "))
    Resultado_suma = suma_dos_numeros(Num1, Num2)
    print(f"La suma de {Num1} y {Num2} es: {Resultado_suma}")
if __name__ == "__main__":
    main()