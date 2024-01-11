Palabra1 = input("Primera palabra: ")
Palabra2 = input("Segunda palabra: ")
if len(Palabra1) >= 2 and len(Palabra2) >= 2:
    nueva1 = Palabra2[:1] + Palabra1[1:]
    nueva2 = Palabra1[:1] + Palabra2[1:]
    print(f"Palabras intercambiadas: {nueva1}, {nueva2}")
else:
    print("Hay menos de dos caracteres por palabra.")
