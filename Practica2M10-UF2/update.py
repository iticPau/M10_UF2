from conection import cursor,conn
#Esta es la funcion para actualizar las motos en la bd
def actualizar_motos():
    #En esta consulta actualizamos el nombre de la moto que pasamos por ID
    consulta = ''' UPDATE public.motos SET moto_nombre='CBR300' WHERE moto_id='1'
    '''
    #Ejecuta la consulta SQL utilizando el cursor
    cursor.execute(consulta)
    #Confirma los cambios en la bd
    conn.commit()
    #Cierra el cursor
    cursor.close()
    #Cierra la conexion a la bd
    conn.close()
