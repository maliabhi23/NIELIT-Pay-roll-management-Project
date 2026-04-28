from sqlalchemy import Column, Integer, String
from app.database import Base

class Leave(Base):
    __tablename__ = "leaves"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    reason = Column(String)
    from_date = Column(String)
    to_date = Column(String)
    status = Column(String, default="Pending")