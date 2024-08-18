import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='meu_banco',
            user='root',
            password='789456'
        )

        if connection.is_connected():
            print("Conexão com MySQL estabelecida com sucesso")
            return connection

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Conexão com MySQL encerrada")

conn = create_connection()
if conn:
    close_connection(conn)

# Output esperado:
# Conexão com MySQL estabelecida com sucesso
# Conexão com MySQL encerrada