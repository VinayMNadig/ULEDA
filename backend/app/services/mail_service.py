import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config.settings import settings


class MailService:

    @staticmethod
    def send_otp(receiver_email: str, otp: str):

        subject = "ULEDA Database Approval OTP"

        body = f"""
Hello,

A database modification request has been received.

Your One-Time Password (OTP) is:

{otp}

This OTP is valid for 5 minutes.

If you did not request this approval, please ignore this email.

Regards,
ULEDA AI Database Assistant
"""

        message = MIMEMultipart()

        message["From"] = settings.EMAIL_ADDRESS
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(
            settings.SMTP_SERVER,
            settings.SMTP_PORT,
        )

        server.starttls()

        server.login(
            settings.EMAIL_ADDRESS,
            settings.EMAIL_PASSWORD,
        )

        server.send_message(message)

        server.quit()

        return True


mail_service = MailService()