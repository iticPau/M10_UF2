from conection import cursor,conn
#Esta es la funcion para borrar motos en la bd
def borrar_motos():
    #Aqui borramos la moto por ID
    consulta = ''' DELETE FROM public.motos WHERE moto_id='1'
    '''
    #Ejecuta la consulta SQL utilizando el cursor
    cursor.execute(consulta)
    #Confirma los cambios en la bd
    conn.commit()
    #Cierra el cursor
    cursor.close()
    #Cierra la conexion a la bd
    conn.close()
