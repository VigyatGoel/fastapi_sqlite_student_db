from contextlib import asynccontextmanager

from fastapi import FastAPI, Query

from my_app.database.database import database
from my_app.services.services import StatusEnum, BranchEnum, insert_into_db_service, update_in_db_service, \
    delete_from_db_service, \
    get_all_from_db_service, get_from_db_using_id_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"message": "Welcome to Students database API."}


@app.get("/help")
async def get_help():
    return {
        "name": "Students database API",
        "version": 1.0,
        "database": "Sqlite"
    }


@app.post("/insert_student/")
async def insert_student(
        student_id: int = Query(...),
        branch: BranchEnum = Query(...),
        cgpa: float = Query(...),
        status: StatusEnum = Query(...)
):
    await insert_into_db_service(
        student_id=student_id,
        branch=branch,
        cgpa=cgpa,
        status=status
    )
    return {
        "response": "ok"
    }


@app.put("/update_student/")
async def update_student(
        student_id: int = Query(...),
        branch: BranchEnum = Query(...),
        cgpa: float = Query(...),
        status: StatusEnum = Query(...)
):
    await update_in_db_service(
        student_id=student_id,
        branch=branch,
        cgpa=cgpa,
        status=status
    )
    return {
        "response": "ok"
    }


@app.delete("/delete_student/")
async def delete_student(student_id: int = Query(...)):
    await delete_from_db_service(student_id)
    return {
        "response": "ok"
    }


@app.get("/get_all_students/")
async def get_all_students():
    students = await get_all_from_db_service()
    return {"students": students}


@app.get("/get_student/{student_id}")
async def get_student_by_id(student_id: int):
    student = await get_from_db_using_id_service(student_id)
    return {"student": student}
