from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models.employee import Employee
from app.models.leave import Leave
from app.models.payroll import Payroll

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    employee_count = db.query(Employee).count()

    pending_leaves = db.query(Leave).filter(
        Leave.status == "Pending"
    ).count()

    current_month = datetime.now().strftime("%B %Y")

    payroll_rows = db.query(Payroll).filter(
        Payroll.month == current_month
    ).all()

    payroll_count = len(payroll_rows)

    total_salary = sum(
        row.net_salary for row in payroll_rows
    )

    return {
        "employees": employee_count,
        "pending_leaves": pending_leaves,
        "payroll_processed": payroll_count,
        "current_month": current_month,
        "current_month_salary_paid": total_salary
    }