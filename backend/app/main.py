from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models import user, employee, leave, attendance, payroll

from app.routes.auth import router as auth_router
from app.routes.employee import router as employee_router
from app.routes.leave import router as leave_router
from app.routes.payroll import router as payroll_router
from app.routes.reports import router as reports_router
from app.routes.ai import router as ai_router


app = FastAPI(
    title="NIELIT Payroll Portal",
    version="1.0"
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(leave_router)
app.include_router(payroll_router)
app.include_router(reports_router)
app.include_router(ai_router)


@app.get("/")
def home():
    return {
        "message": "NIELIT Payroll Portal Running Successfully"
    }