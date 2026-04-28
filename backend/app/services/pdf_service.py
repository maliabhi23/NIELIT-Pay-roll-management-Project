import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

PDF_DIR = "generated_payslips"
os.makedirs(PDF_DIR, exist_ok=True)


def generate_payslip(employee_name, payroll_row):
    filename = f"{PDF_DIR}/{employee_name}_{payroll_row.month}.pdf"

    c = canvas.Canvas(filename, pagesize=A4)

    gross = payroll_row.gross
    pf = payroll_row.pf
    tax = payroll_row.tax
    leave_deduction = payroll_row.leave_deduction
    total_deduction = pf + tax + leave_deduction
    net_salary = payroll_row.net_salary

    basic = gross * 0.65
    da = gross * 0.15
    hra = gross * 0.12
    bonus = gross * 0.08

    LEFT_X = 55
    RIGHT_X = 285   # moved left (before 330)

    y = 810

    c.setFont("Helvetica-Bold", 15)
    c.drawString(
        LEFT_X,
        y,
        "National Institute Of Electronics and Information Technology (NIELIT)"
    )

    y -= 28
    c.setFont("Helvetica", 11)
    c.drawString(
        LEFT_X,
        y,
        f"Salary Slip for the month of {payroll_row.month}"
    )

    y -= 35
    c.setFont("Helvetica-Bold", 11)
    c.drawString(
        LEFT_X,
        y,
        f"GROSS PAY : Rs.{round(gross,2)}"
    )
    c.drawString(
        RIGHT_X,
        y,
        f"TOTAL DEDUCTIONS : Rs.{round(total_deduction,2)}"
    )

    y -= 28
    c.setFont("Helvetica-Bold", 12)
    c.drawString(
        LEFT_X,
        y,
        f"Net Salary : Rs.{round(net_salary,2)} deposited in Saving Bank A/C"
    )

    y -= 40
    c.setFont("Helvetica", 10)
    c.drawString(LEFT_X, y, "Employee ID : EMP001")
    y -= 20
    c.drawString(LEFT_X, y, f"Employee Name : {employee_name}")
    y -= 20
    c.drawString(LEFT_X, y, "Designation : Software Engineer")
    y -= 20
    c.drawString(LEFT_X, y, "Department : IT Department")

    y -= 35
    c.setFont("Helvetica-Bold", 11)
    c.drawString(LEFT_X, y, "PAY & ALLOWANCES")
    c.drawString(RIGHT_X, y, "DEDUCTIONS")

    y -= 28
    c.setFont("Helvetica", 10)

    left = [
        f"Basic Pay : Rs.{round(basic,2)}",
        f"Dearness Allowance : Rs.{round(da,2)}",
        f"HRA : Rs.{round(hra,2)}",
        f"Bonus : Rs.{round(bonus,2)}",
    ]

    right = [
        f"PF : Rs.{round(pf,2)}",
        f"Income Tax : Rs.{round(tax,2)}",
        f"Leave Deduction : Rs.{round(leave_deduction,2)}",
        "Other Deduction : Rs.0",
    ]

    for l, r in zip(left, right):
        c.drawString(LEFT_X, y, l)
        c.drawString(RIGHT_X, y, r)
        y -= 22

    y -= 10
    c.line(LEFT_X, y, 540, y)

    y -= 28
    c.setFont("Helvetica-Bold", 12)
    c.drawString(
        LEFT_X,
        y,
        f"Final Net Salary : Rs.{round(net_salary,2)}"
    )

    y -= 50
    c.setFont("Helvetica", 10)
    c.drawString(
        LEFT_X,
        y,
        "This is a computer generated salary slip."
    )

    c.save()
    return filename