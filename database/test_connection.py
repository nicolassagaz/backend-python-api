from connection import get_connection

connection = get_connection()

print("Conexão realizada com sucesso!")

connection.close()