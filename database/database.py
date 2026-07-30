import sqlite3


DATABASE_NAME = "school_payment.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    with open("database/schema.sql", "r") as file:
        connection.executescript(file.read())

    connection.commit()
    connection.close()