import psycopg2


def get_connection():

    connection = psycopg2.connect(
        host="localhost",
        database="tickets_db",
        user="postgres",
        password="10pilares"
    )

    return connection