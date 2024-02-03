from conection import conn, cursor
#Esta es la funcion para crear la tabla de motos en la bd
def crear_motos():
    #Esta es la consulta SQL para crear la tabla MOTOS con sus columnas
    consulta = '''CREATE TABLE MOTOS(
                    moto_id SERIAL PRIMARY KEY,
                    moto_nombre VARCHAR(255) NOT NULL,
                    moto_matricula VARCHAR(255) NOT NULL,
                    moto_HP INT NOT NULL,
                    moto_marca VARCHAR(255) NOT NULL,
                    moto_anyo INT NOT NULL
    )'''

    #Ejecuta la consulta SQL utilizando el cursor
    cursor.execute(consulta)
    #Confirma los cambios en la bd
    conn.commit()
    #Cierra el cursor
    cursor.close()
    #Cierra la conexion a la bd
    conn.close()