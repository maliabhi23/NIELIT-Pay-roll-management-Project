from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    emp_code = Column(String, unique=True)
    name = Column(String)
    department = Column(String)
    designation = Column(String)
    email = Column(String)
    phone = Column(String)

    basic_salary = Column(Float)
    hra = Column(Float)
    da = Column(Float)
    bonus = Column(Float)