def main():
    Dicc_contactos = {}
    while True:
        Nombre = input("Introduce un nombre (o fin para mostrar la lista de contactos): ")
        if Nombre.lower() == 'fin':
            break
        if Nombre in Dicc_contactos:
            print(f"El nombre {Nombre} ya existe en el diccionario. No se agrega.")
        else:
            try:
                Edad = int(input(f"Introduce la edad para {Nombre}: "))
                Dicc_contactos[Nombre] = Edad
            except ValueError:
                print("Por favor introduce una edad.")
    print("Diccionario de contactos:")
    for Nombre, Edad in Dicc_contactos.items():
        print(f"{Nombre}: {Edad} años")
if __name__ == "__main__":
    main()
