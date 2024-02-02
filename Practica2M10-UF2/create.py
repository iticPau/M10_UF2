from conection import cursor,conn
consulta_insert = ''' INSERT INTO public.motos(moto_id,moto_name,moto_matricula,moto_HP)
                            VALUES('1','Kawasaki Ninja','9180525H3A','44')

'''

cursor.execute(consulta_insert)
conn.commit()