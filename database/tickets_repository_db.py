from connection import get_connection

def find_all():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute( "SELECT * FROM tickets")

    tickets = cursor.fetchall()

    cursor.close()

    connection.close()

    return tickets

def create(title, description, priority):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tickets
        (
            title,
            description,
            priority,
            status
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s
        )
        """,
        (
            title,
            description,
            priority,
            "Aberto"
        )
    )

    connection.commit()

    cursor.close()

    connection.close()