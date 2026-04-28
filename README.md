# NIELIT Payroll Portal

A full-stack Payroll Management System developed as a Final Year Major Project for automating employee payroll operations, leave approvals, salary processing, PDF payslip generation, email automation, reporting, and AI-assisted administrative insights.

---

# Project Overview

NIELIT Payroll Portal is a web-based payroll automation platform designed to simplify and digitize salary management processes within an organization.

The system enables administrators to:

* Manage employees
* Process salaries automatically
* Approve / reject leave requests
* Generate professional salary slips in PDF format
* Send payslips through email
* View monthly reports
* Interact with an AI Assistant for payroll insights

This project demonstrates real-world HR and payroll workflow automation.

---

# Features

## Admin Module

* Admin Login Authentication
* Dashboard Analytics
* Add Employee
* View Employees
* Delete Employee
* Apply Leave Management
* Approve Leave
* Reject Leave
* Process Salary
* Auto Payroll Calculation
* PDF Payslip Generation
* Email Payslip Automation
* Reports Module
* Monthly Salary Summary
* AI Payroll Assistant
* Logout

---

## Payroll Calculation

Net Salary is calculated automatically:

Net Salary = Gross Salary - PF - Tax - Leave Deduction

Where:

Gross Salary = Basic Salary + HRA + DA + Bonus

Deductions:

* PF = 12%
* Tax = 5%
* Leave Deduction = configurable

---

# AI Assistant Module

The AI Assistant enables admin to ask:

* Who got highest salary this month?
* Total employees?
* Pending leaves?
* Total payroll this month?
* Who took most leaves?

The assistant analyzes payroll database records and returns intelligent responses.

Future enhancement:
Integration with real Generative AI / LLM models.

---

# Tech Stack

## Backend

* FastAPI
* SQLite
* SQLAlchemy ORM
* JWT Authentication
* ReportLab PDF Generation
* SMTP Email Automation

## Frontend

* React
* Vite
* Axios
* React Toastify
* CSS

---

# System Modules

1. Authentication Module
2. Employee Management Module
3. Leave Management Module
4. Payroll Processing Module
5. Payslip Generation Module
6. Email Notification Module
7. Reports Module
8. AI Assistant Module

---

# Project Structure

```text
## Project Structure

```text
NIELIT-PAYROLL-PORTAL/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── attendance.py
│   │   │   ├── employee.py
│   │   │   ├── leave.py
│   │   │   ├── payroll.py
│   │   │   └── user.py
│   │   │
│   │   ├── routes/
│   │   │   ├── ai.py
│   │   │   ├── auth.py
│   │   │   ├── employee.py
│   │   │   ├── leave.py
│   │   │   ├── payroll.py
│   │   │   └── reports.py
│   │   │
│   │   ├── schemas/
│   │   │
│   │   ├── services/
│   │   │   ├── email_service.py
│   │   │   └── pdf_service.py
│   │   │
│   │   ├── utils/
│   │   │   └── security.py
│   │   │
│   │   ├── config.py
│   │   ├── database.py
│   │   └── main.py
│   │
│   ├── generated_payslips/
│   ├── .env
│   ├── payroll.db
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── public/
│   │
│   ├── src/
│   │   │
│   │   ├── assets/
│   │   │
│   │   ├── components/
│   │   │   ├── AIAssistant.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── EmployeeTable.jsx
│   │   │   ├── LeaveTable.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── PayrollTable.jsx
│   │   │   └── Sidebar.jsx
│   │   │
│   │   ├── api.js
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   ├── main.jsx
│   │   └── styles.css
│   │
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   └── vite.config.js
│
├── README.md
│
└── .gitignore
```
```

---

# Installation

## Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

Create Admin:

POST:

```text
/auth/seed-admin
```

Default Credentials:

```text
username: admin
password: admin123
```

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# Future Scope

* Employee Portal
* Attendance Tracking
* Bank API Integration
* Real Generative AI Chatbot
* Fraud Detection
* Salary Forecasting
* Department Analytics
* Cloud Deployment

---

# Academic Relevance

This project combines:

* Software Engineering
* Artificial Intelligence concepts
* Web Development
* Database Management
* Automation


---
NIELIT Payroll Portal

