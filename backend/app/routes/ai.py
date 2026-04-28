from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import requests

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
    question = data.get("question", "")
    history = data.get("history", [])

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

    highest_salary = 0
    highest_emp = None
    highest_emp_name = "Unknown"

    if payroll_rows:
        top = max(
            payroll_rows,
            key=lambda x: x.net_salary
        )

        highest_salary = top.net_salary
        highest_emp = top.employee_id

        emp = db.query(Employee).filter(
            Employee.id == top.employee_id
        ).first()

        if emp:
            highest_emp_name = emp.name

    chat_history = "\n".join([
        f"{m['role']}: {m['text']}"
        for m in history[-10:]
    ])

    prompt = f"""
You are payroll AI assistant.

Payroll information:
Total employees: {employee_count}
Pending leaves: {pending_leaves}
Current month: {current_month}
Total salary paid: ₹{round(total_salary,2)}
Highest salary: ₹{round(highest_salary,2)}
Highest salary employee name: {highest_emp_name}

Conversation:
{chat_history}

Reply professionally and clearly.
"""

    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:3b",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        result = res.json()

        answer = (
            result.get("response")
            or result.get("message", {}).get("content")
            or "No response"
        )

    except Exception as e:
        answer = f"Ollama Error: {str(e)}"

    return {
        "answer": answer
    }