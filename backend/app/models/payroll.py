from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class Payroll(Base):
    __tablename__ = "payroll"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)

    gross = Column(Float)
    pf = Column(Float)
    tax = Column(Float)
    leave_deduction = Column(Float)
    net_salary = Column(Float)

    month = Column(String)