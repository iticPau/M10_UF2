#-*- coding: utf-8 -*-
try:
    #Importa las funciones del CRUD desde los archivos x.py
    from create_table import crear_motos
    from create import insertar_motos
    from read import consultar_motos
    from update import actualizar_motos
    from delete import borrar_motos
    
    #Muestra el menu que te creado extra ,donde define las funciones para ejecutar la opcion seleccionada
    def menu():
        while True:
            print("a - Crear tabla de motos")
            print("b - Insertar motos")
            print("c - Consultar motos")
            print("d - Actualizar motos")
            print("e - Borrar motos")
            print("q - Salir")

            opcion = input("Selecciona una opcion:")

            if opcion == 'a':
                crear_motos()
            elif opcion == 'b':
                insertar_motos()
            elif opcion == 'c':
                consultar_motos()
            elif opcion == 'd':
                actualizar_motos()
            elif opcion == 'e':
                borrar_motos()
            elif opcion == 'q':
                print("Salir del programa")
                break
            else:
                print("Opcion incorrecta")

    #Comprueba si el script esta siendo ejecutado
    if __name__ == "__main__":
        menu()

except Exception as e:
    #Controla cualquier excepcion que pueda ocurrir durante la ejecuccion
    print(f"Error en la ejecuccion por favor intentalo de nuevo: {str(e)}")