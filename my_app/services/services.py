from enum import Enum
from sqlite3 import IntegrityError, DatabaseError

from fastapi import HTTPException

from my_app.database.database import insert_into_db, update_in_db, delete_from_db, get_all_from_db, get_from_db_using_id


class StatusEnum(str, Enum):
    Pass = "Pass"
    Fail = "Fail"


class BranchEnum(str, Enum):
    CS = "CS"
    IT = "IT"
    ECE = "ECE"
    MCE = "MCE"


async def insert_into_db_service(student_id: int, branch: str, cgpa: float, status: StatusEnum):
    try:
        await insert_into_db(
            student_id=student_id,
            branch=branch,
            cgpa=cgpa,
            status=status
        )
    except IntegrityError:
        raise HTTPException(status_code=500, detail="student_id already exists.")
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")


async def update_in_db_service(student_id: int, branch: str, cgpa: float, status: str):
    try:
        await update_in_db(
            student_id=student_id,
            branch=branch,
            cgpa=cgpa,
            status=status
        )
    except ValueError:
        raise HTTPException(status_code=404, detail="no student found with given student_id.")
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")


async def delete_from_db_service(student_id: int):
    try:
        # Check if the student exists before attempting to delete
        student = await get_from_db_using_id(student_id)
        if not student:
            raise HTTPException(status_code=404, detail=f"Student with ID {student_id} does not exist.")
        await delete_from_db(student_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting from database: {e}")


async def get_all_from_db_service():
    try:
        return await get_all_from_db()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")


async def get_from_db_using_id_service(student_id: int):
    try:
        student = await get_from_db_using_id(student_id)
        if not student:
            raise HTTPException(status_code=404, detail=f"Student with ID {student_id} does not exist.")
        return student

    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
