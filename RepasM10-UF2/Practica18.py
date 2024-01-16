print("Escribe dos palabras para contar sus letras:")
Palabras = input().split()
Tupla = tuple(Palabras)
letraCon = {}
for palabra in Tupla:
    for letra in palabra:
        if letra in letraCon:
            letraCon[letra] += 1
        else:
            letraCon[letra] = 1
print("\nLetras contadas:")
for letra, frecuencia in letraCon.items():
    print(f"{letra}: {frecuencia}")