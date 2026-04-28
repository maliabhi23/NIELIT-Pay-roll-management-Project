from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models.employee import Employee
from app.models.leave import Leave
from app.models.payroll import Payroll

router = APIRouter(
    prefix="/ai",
    tags=["AI Assistant"]
)


@router.post("/ask")
def ask_ai(data: dict, db: Session = Depends(get_db)):
    question = data.get("question", "").lower()

    employee_count = db.query(Employee).count()

    pending_leaves = db.query(Leave).filter(
        Leave.status == "Pending"
    ).count()

    current_month = datetime.now().strftime("%B %Y")

    payroll_rows = db.query(Payroll).filter(
        Payroll.month == current_month
    ).all()

    total_salary = sum(
        row.net_salary for row in payroll_rows
    )

    if "total employees" in question:
        return {
            "answer": f"Total employees are {employee_count}"
        }

    if "pending leave" in question:
        return {
            "answer": f"Pending leave requests are {pending_leaves}"
        }

    if "total payroll" in question or "salary paid" in question:
        return {
            "answer": (
                f"Total salary paid in {current_month} "
                f"is ₹ {round(total_salary,2)}"
            )
        }

    if "highest salary" in question:
        if not payroll_rows:
            return {
                "answer": "No payroll processed this month"
            }

        highest = max(
            payroll_rows,
            key=lambda x: x.net_salary
        )

        return {
            "answer": (
                f"Highest salary this month is ₹ "
                f"{round(highest.net_salary,2)} "
                f"for employee id {highest.employee_id}"
            )
        }

    if "most leave" in question:
        leaves = db.query(Leave).all()

        counter = {}
        for row in leaves:
            counter[row.employee_id] = (
                counter.get(row.employee_id, 0) + 1
            )

        if not counter:
            return {
                "answer": "No leave records found"
            }

        top = max(
            counter,
            key=counter.get
        )

        return {
            "answer": (
                f"Employee id {top} "
                f"has highest leaves ({counter[top]})"
            )
        }

    return {
        "answer": (
            "I can answer: total employees, pending leaves, "
            "highest salary, total payroll, most leave"
        )
    }