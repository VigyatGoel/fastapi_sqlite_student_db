import os

from sqlalchemy import create_engine

from my_app.models.model import metadata, student_table

# Define the path to the database within the my_app/database directory
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "database", "students.db"))
DATABASE_URL = f"sqlite:///{db_path}"


def setup_database():
    engine = create_engine(DATABASE_URL)

    with engine.connect() as connection:
        if engine.dialect.has_table(connection, "student_table"):
            print("Table exists. Dropping table...")
            student_table.drop(connection)
            print("Table dropped.")
        print("Creating table...")
        metadata.create_all(engine)
        print("Table created.")


if __name__ == "__main__":
    setup_database()
