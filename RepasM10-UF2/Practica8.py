Palabras = input("Introduce entre 1 y 3: ")
lista_palabras = Palabras.split()
cantidad_palabras = len(lista_palabras)
if 1 <= cantidad_palabras <= 3:
    for palabra in lista_palabras:
        print(f"Palabra: {palabra}")
        print(f"Numero de caracteres: {len(palabra)}")
        print(f"Primer carácter: {palabra[0]}")
        print(f"Último carácter: {palabra[-1]}")
else:
        print("Hay mas de 3 palabras")    
