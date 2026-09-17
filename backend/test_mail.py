from app.services.mail_service import mail_service

mail_service.send_otp(
    receiver_email="vinaym24cs@rnsit.ac.in",
    otp="583921"
)

print("OTP Sent Successfully!")