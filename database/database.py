import sqlite3

DATABASE_NAME = "school_payment.db"


def connect_database():
    """Create and return a database connection."""
    return sqlite3.connect(DATABASE_NAME)


def create_database():
    """Create the database tables if they don't already exist."""
    connection = connect_database()

    with open("database/schema.sql", "r") as file:
        connection.executescript(file.read())

    connection.commit()
    connection.close()


def save_student(student_id, name, student_class, school_fee):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students
        (student_id, name, student_class, school_fee)
        VALUES (?, ?, ?, ?)
        """,
        (student_id, name, student_class, school_fee)
    )

    connection.commit()
    connection.close()


def get_student(student_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE student_id = ?
        """,
        (student_id,)
    )

    student = cursor.fetchone()

    connection.close()

    return student


def save_student(student_id, name, student_class, school_fee):
    connection = connect_database()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO students
            (student_id, name, student_class, school_fee)
            VALUES (?, ?, ?, ?)
            """,
            (student_id, name, student_class, school_fee)
        )

        connection.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        connection.close()


def get_payments(student_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT amount, payment_date
        FROM payments
        WHERE student_id = ?
        ORDER BY payment_date
        """,
        (student_id,)
    )

    payments = cursor.fetchall()

    connection.close()

    return payments
