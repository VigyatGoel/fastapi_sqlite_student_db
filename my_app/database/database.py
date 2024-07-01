import os

from databases import Database

from my_app.models.model import student_table

DATABASE_URL = "sqlite:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "students.db"))
database = Database(DATABASE_URL)


async def insert_into_db(student_id: int, branch: str, cgpa: float, status: str):
    query = student_table.insert().values(
        student_id=student_id,
        branch=branch,
        cgpa=cgpa,
        status=status
    )
    await database.execute(query)


async def update_in_db(student_id: int, branch: str, cgpa: float, status: str):
    query = student_table.update().where(student_table.c.student_id == student_id).values(student_id=student_id,
                                                                                          branch=branch, cgpa=cgpa,
                                                                                          status=status)
    await database.execute(query)


async def delete_from_db(student_id: int):
    query = student_table.delete().where(student_table.c.student_id == student_id)
    return await database.execute(query)


async def get_all_from_db():
    query = student_table.select()
    return await database.fetch_all(query)


async def get_from_db_using_id(student_id: int):
    query = student_table.select().where(student_table.c.student_id == student_id)
    return await database.fetch_one(query)
