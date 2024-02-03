from conection import cursor,conn
#Esta es la funcion para cosultar la tabla de motos en la bd
def consultar_motos():
    #Esta seria la consulta donde nos muestra las motos que hay en la tabla
    consulta = ''' SELECT moto_id, moto_nombre, moto_matricula, moto_HP, moto_marca, moto_anyo
                    FROM public.motos
    '''
    #Ejecuta la consulta SQL utilizando el cursor
    cursor.execute(consulta)
    #Cierra el cursor
    cursor.close()
    #Cierra la conexion a la bd
    conn.close()
