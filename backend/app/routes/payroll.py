from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.employee import Employee
from app.models.payroll import Payroll

from app.services.pdf_service import generate_payslip
from app.services.email_service import send_payslip

router = APIRouter(prefix="/payroll", tags=["Payroll"])


@router.post("/process/{employee_id}")
def process_salary(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not emp:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    gross = emp.basic_salary + emp.hra + emp.da + emp.bonus
    pf = gross * 0.12
    tax = gross * 0.05
    leave_deduction = 0
    net_salary = gross - pf - tax - leave_deduction

    row = Payroll(
        employee_id=employee_id,
        gross=gross,
        pf=pf,
        tax=tax,
        leave_deduction=leave_deduction,
        net_salary=net_salary,
        month="May 2026"
    )

    db.add(row)
    db.commit()
    db.refresh(row)

    pdf_file = generate_payslip(
        emp.name,
        row
    )

    email_status = "Not Sent"

    try:
        send_payslip(
            emp.email,
            pdf_file
        )
        email_status = "Mail Sent Successfully"
    except Exception as e:
        email_status = f"Mail Failed: {str(e)}"

    return {
        "message": "Payroll processed successfully",
        "employee_name": emp.name,
        "employee_email": emp.email,
        "pdf_generated": pdf_file,
        "email_status": email_status,
        "gross_salary": gross,
        "pf": pf,
        "tax": tax,
        "net_salary": net_salary
    }


@router.get("/")
def get_payroll(db: Session = Depends(get_db)):
    rows = db.query(Payroll).all()

    return [
        {
            "employee_id": r.employee_id,
            "gross": r.gross,
            "pf": r.pf,
            "tax": r.tax,
            "leave_deduction": r.leave_deduction,
            "net_salary": r.net_salary,
            "month": r.month
        }
        for r in rows
    ]