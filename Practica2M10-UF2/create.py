from conection import cursor,conn
#Esta es la funcion para insertar motos en la bd
def insertar_motos(moto_id, moto_nombre, moto_matricula, moto_HP, moto_marca, moto_anyo):
    #Aqui esta la consulta que esta insertando una motod a la bd
    consulta = ''' INSERT INTO public.motos(moto_id,moto_nombre,moto_matricula,moto_HP,moto_marca,moto_anyo)
                            VALUES('1','Ninja','9180525H3A','44','Kawasaki','2016')
    '''
    #Ejecuta la consulta SQL utilizando el cursor
    cursor.execute(consulta)
    #Confirma los cambios en la bd
    conn.commit()
    #Cierra el cursor
    cursor.close()
    #Cierra la conexion a la bd
    conn.close()