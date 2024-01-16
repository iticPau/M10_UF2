# Creamos una tupla con los meses del año
Meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
while True:
        Num = int(input("Ingresa un numero entre el 1-12: "))
        if Num == 0:
            print("Programa finalizado")
            break
        elif 0 < Num <= 12:
            print(f"El mes {Num} es:" , Meses[Num - 1])
      