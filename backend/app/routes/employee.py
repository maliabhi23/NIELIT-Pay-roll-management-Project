from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.employee import Employee

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    rows = db.query(Employee).all()

    return [
        {
            "id": e.id,
            "emp_code": e.emp_code,
            "name": e.name,
            "department": e.department,
            "designation": e.designation,
            "email": e.email,
            "phone": e.phone,
            "basic_salary": e.basic_salary,
            "hra": e.hra,
            "da": e.da,
            "bonus": e.bonus
        }
        for e in rows
    ]


@router.post("/")
def add_employee(data: dict, db: Session = Depends(get_db)):
    emp = Employee(
        emp_code=data["emp_code"],
        name=data["name"],
        department=data["department"],
        designation=data["designation"],
        email=data["email"],
        phone=data["phone"],
        basic_salary=data["basic_salary"],
        hra=data["hra"],
        da=data["da"],
        bonus=data["bonus"]
    )

    db.add(emp)
    db.commit()

    return {"message": "Employee added successfully"}


@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    data: dict,
    db: Session = Depends(get_db)
):
    emp = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not emp:
        raise HTTPException(404, "Employee not found")

    emp.name = data["name"]
    emp.department = data["department"]
    emp.designation = data["designation"]
    emp.email = data["email"]
    emp.phone = data["phone"]
    emp.basic_salary = data["basic_salary"]
    emp.hra = data["hra"]
    emp.da = data["da"]
    emp.bonus = data["bonus"]

    db.commit()

    return {"message": "Employee updated successfully"}


@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    emp = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not emp:
        raise HTTPException(404, "Employee not found")

    db.delete(emp)
    db.commit()

    return {"message": "Employee deleted successfully"}