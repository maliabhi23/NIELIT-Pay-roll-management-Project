from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/seed-admin")
def seed_admin(db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == "admin").first()

    if existing:
        return {"message": "Admin already exists"}

    admin = User(
        username="admin",
        email="admin@nielit.com",
        password=hash_password("admin123"),
        role="admin"
    )

    db.add(admin)
    db.commit()

    return {
        "message": "Admin created",
        "username": "admin",
        "password": "admin123"
    }


@router.post("/create-employee-login")
def create_employee_login(data: dict, db: Session = Depends(get_db)):
    user = User(
        username=data["username"],
        email=data["email"],
        password=hash_password(data["password"]),
        role="employee"
    )

    db.add(user)
    db.commit()

    return {"message": "Employee login created"}


@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):
    username = data.get("username")
    password = data.get("password")

    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user:
        raise HTTPException(401, "Invalid username")

    if not verify_password(password, user.password):
        raise HTTPException(401, "Invalid password")

    token = create_access_token({
        "sub": user.username,
        "role": user.role
    })

    return {
        "access_token": token,
        "role": user.role,
        "username": user.username
    }