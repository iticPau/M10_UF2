import psycopg2

conn = psycopg2.connect(
    database="postgresDB",
    user="123",
    password="admin",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()
print(cursor)