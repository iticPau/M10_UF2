from conection import conn,cursor
consulta = '''CREATE TABLE MOTOS(
                moto_id SERIAL PRIMARY KEY,
                moto_name VARCHAR(255) NOT NULL,
                moto_matricula INT NOT NULL,
                moto_HP INT NOT NULL
)'''

cursor.execute(consulta)
conn.commit()