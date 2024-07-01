from sqlalchemy import MetaData, Table, Column, Integer, String, Float

metadata = MetaData()

student_table = Table(
    "student_table",
    metadata,
    Column("student_id", Integer, unique=True, nullable=False, primary_key=True),
    Column("branch", String(4), nullable=False),
    Column("cgpa", Float, nullable=False),
    Column("status", String(1), nullable=False)
)
