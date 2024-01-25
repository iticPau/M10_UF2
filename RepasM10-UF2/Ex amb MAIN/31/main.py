from Practica31 import calcular_iva
def main():
    Cantidad_sin_iva = float(input("Escriba la cantidad sin IVA : "))
    Iva_porcentaje = int(input("Introduce el porcentaje de IVA (4%, 10% o 21%): "))
    calcular_iva(Cantidad_sin_iva, Iva_porcentaje)
if __name__ == "__main__":
    main()