# NIELIT Payroll Portal

A full-stack AI-powered Payroll Management System developed for automating employee payroll operations, leave approvals, salary processing, PDF payslip generation, email automation, reporting, and Generative AI-assisted administrative insights.

---

# Project Overview

NIELIT Payroll Portal is a web-based payroll automation platform designed to simplify and digitize salary management processes within an organization.

The system enables administrators to:

* Manage employees
* Process salaries automatically
* Approve / Reject leave requests
* Generate professional salary slips in PDF format
* Send payslips through email
* View monthly reports
* Interact with an AI Payroll Assistant
* Generate payroll insights using Generative AI

This project demonstrates real-world HR, Payroll Automation, and AI integration.

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
* AI Payroll Chat Assistant
* Logout

---

# Payroll Calculation

Net Salary is calculated automatically:

```text id="rd1"
Net Salary = Gross Salary - PF - Tax - Leave Deduction
```

Where:

```text id="rd2"
Gross Salary = Basic Salary + HRA + DA + Bonus
```

Deductions:

* PF = 12%
* Tax = 5%
* Leave Deduction = configurable

---

# AI Assistant Module (Generative AI)

The AI Assistant enables admin to ask:

* Who got highest salary this month?
* Total employees?
* Pending leaves?
* Total payroll this month?
* Who took most leaves?
* Explain payroll increase this month
* Generate payroll summary report

## AI Working

```text id="rd3"
Payroll Database
      ↓
Context Building
      ↓
Prompt Engineering
      ↓
Google Gemini API
      ↓
Natural Language AI Response
```

## Gemini Integration Features

* Payroll insight generation
* Salary trend explanation
* Natural language reporting
* Employee payroll analytics
* Smart administrative Q&A
* AI-based summary generation

This converts the project into a **real Generative AI Powered Payroll Management System**.

---

# Tech Stack

## Backend

* FastAPI
* SQLite
* SQLAlchemy ORM
* JWT Authentication
* ReportLab PDF Generation
* SMTP Email Automation
* REST API
* Generative AI Integration

## Frontend

* React
* Vite
* Axios
* React Toastify
* CSS

## AI Stack

* Google Gemini API
* Prompt Engineering
* Context-aware Querying
* Natural Language Response Generation

---

# Google Gemini API Configuration

To enable Generative AI features:

Create:

```text id="rd4"
backend/.env
```

Add:

```env id="rd5"
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
SECRET_KEY=nielit_secret_key

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password
```

Install dependency:

```bash id="rd6"
pip install google-generativeai
```

or:

```bash id="rd7"
pip install -r requirements.txt
```

How it works:

```text id="rd8"
Admin asks question
      ↓
FastAPI receives query
      ↓
Payroll database context collected
      ↓
Prompt sent to Google Gemini API
      ↓
Gemini generates intelligent answer
      ↓
Answer shown in AI Chat UI
```

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
9. Generative AI Module

---

# Project Structure

```text id="rd9"
NIELIT-PAYROLL-PORTAL/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── main.py
│   ├── generated_payslips/
│   ├── .env
│   ├── payroll.db
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── .gitignore
```

---

# Installation

## Backend Setup

```bash id="rd10"
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend URL:

```text id="rd11"
http://127.0.0.1:8000
```

Swagger Docs:

```text id="rd12"
http://127.0.0.1:8000/docs
```

Create Admin:

```text id="rd13"
POST /auth/seed-admin
```

Default Credentials:

```text id="rd14"
username: admin
password: admin123
```

---

## Frontend Setup

```bash id="rd15"
cd frontend
npm install
npm run dev
```

Frontend URL:

```text id="rd16"
http://localhost:5173
```

---

# Future Scope

* Employee Self Service Portal
* Attendance Tracking
* Biometric Integration
* Bank API Integration
* Fraud Detection
* Salary Forecasting using ML
* Department Analytics
* Cloud Deployment
* AI Decision Support System

---

# Project Title Suggestion

**AI-Powered Payroll Management System using FastAPI, React and Google Gemini**
