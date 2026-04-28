import smtplib
from email.message import EmailMessage

from app.config import (
    SMTP_HOST,
    SMTP_PORT,
    SMTP_EMAIL,
    SMTP_PASSWORD
)


def send_payslip(to_email, file_path):
    print("\n========== EMAIL DEBUG ==========")
    print("SMTP_HOST:", SMTP_HOST)
    print("SMTP_PORT:", SMTP_PORT)
    print("FROM:", SMTP_EMAIL)
    print("TO:", to_email)
    print("FILE:", file_path)
    print("================================\n")

    msg = EmailMessage()
    msg["Subject"] = "NIELIT Salary Slip"
    msg["From"] = SMTP_EMAIL
    msg["To"] = to_email

    msg.set_content(
        "Dear Employee,\n\nAttached is your salary slip PDF.\n\nRegards,\nNIELIT"
    )

    with open(file_path, "rb") as f:
        data = f.read()

    msg.add_attachment(
        data,
        maintype="application",
        subtype="pdf",
        filename="Payslip.pdf"
    )

    try:
        print("Connecting SMTP...")
        server = smtplib.SMTP(
            SMTP_HOST,
            SMTP_PORT
        )

        print("Starting TLS...")
        server.starttls()

        print("Logging in...")
        server.login(
            SMTP_EMAIL,
            SMTP_PASSWORD
        )

        print("Sending mail...")
        server.send_message(msg)

        print("Mail sent successfully")
        server.quit()

        return True

    except Exception as e:
        print("EMAIL ERROR:", str(e))
        raise e