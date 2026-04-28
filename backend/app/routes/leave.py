from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.leave import Leave

router = APIRouter(prefix="/leave", tags=["Leave"])


class LeaveRequest(BaseModel):
    employee_id: int
    reason: str
    from_date: str
    to_date: str


@router.post("/apply")
def apply_leave(
    data: LeaveRequest,
    db: Session = Depends(get_db)
):
    lv = Leave(
        employee_id=data.employee_id,
        reason=data.reason,
        from_date=data.from_date,
        to_date=data.to_date,
        status="Pending"
    )

    db.add(lv)
    db.commit()

    return {
        "message": "Leave applied successfully"
    }


@router.get("/")
def get_leave_requests(db: Session = Depends(get_db)):
    rows = db.query(Leave).all()

    return [
        {
            "id": r.id,
            "employee_id": r.employee_id,
            "reason": r.reason,
            "from_date": r.from_date,
            "to_date": r.to_date,
            "status": r.status
        }
        for r in rows
    ]


@router.put("/approve/{leave_id}")
def approve_leave(
    leave_id: int,
    db: Session = Depends(get_db)
):
    lv = db.query(Leave).filter(
        Leave.id == leave_id
    ).first()

    if not lv:
        raise HTTPException(404, "Leave request not found")

    lv.status = "Approved"
    db.commit()

    return {
        "message": "Leave approved successfully"
    }


@router.put("/reject/{leave_id}")
def reject_leave(
    leave_id: int,
    db: Session = Depends(get_db)
):
    lv = db.query(Leave).filter(
        Leave.id == leave_id
    ).first()

    if not lv:
        raise HTTPException(404, "Leave request not found")

    lv.status = "Rejected"
    db.commit()

    return {
        "message": "Leave rejected successfully"
    }