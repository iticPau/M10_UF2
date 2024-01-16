Areas = [
    "Comedor", 10.15, 
    "Recibidor", 9.56, 
    "Habitacion1", 12.34, 
    "Terraza", 15.55, 
    "Lavabo", 7.98, 
    "Cocina", 12, 
    "Habitacion2", 12.23
]
print("El segundo elemento: ", Areas[1])
print("Ultimo elemento: ", Areas[-1])
print("Area de la terraza: ", Areas[7])
print("Del primero al tercer elemento: ", Areas[:4])
print("Del tercer elemento al ultimo: ", Areas[3:])
print("El total de la area de las dos habitaciones: ", Areas[5] + Areas[11])
Areas[9] = 8.76
print("Lavabo modificado: ", Areas)
Areas.extend(["Pati interior", 2.78])
print("Introducir Pati Interior: ", Areas)
