from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.approval_request import ApprovalRequest
from app.security.otp_generator import otp_generator
from app.services.mail_service import mail_service


class ApprovalService:

    # ==========================================
    # Create Approval Request
    # ==========================================

    @staticmethod
    def create_request(
        db: Session,
        question: str,
        sql: str,
        email: str,
    ):

        try:

            print("\n========== APPROVAL ==========")
            print("STEP 1 : Generating OTP")

            otp = otp_generator.generate()

            print("OTP :", otp)

            print("STEP 2 : Creating ApprovalRequest object")

            request = ApprovalRequest(

    user_id=1,

    database_name="company.db",

    question=question,

    sql_query=sql,

    query_type=sql.strip().split()[0].upper(),

    otp=otp,

    status="Pending",

    approved=False,

    attempts=0,

    expires_at=datetime.utcnow() + timedelta(minutes=5),

    approved_by=email,

)

            print("STEP 3 : Saving to database")

            db.add(request)
            db.commit()
            db.refresh(request)

            print("Approval ID :", request.id)

            print("STEP 4 : Sending Email")

            mail_service.send_otp(
                receiver_email=email,
                otp=otp,
            )

            print("STEP 5 : Email Sent Successfully")
            print("==============================\n")

            return request

        except Exception as e:

            db.rollback()

            print("\n========== ERROR ==========")
            print(type(e).__name__)
            print(e)
            print("===========================\n")

            raise e

    # ==========================================
    # Verify OTP
    # ==========================================

    @staticmethod
    def verify_otp(
        db: Session,
        request_id: int,
        otp: str,
    ):

        print("\n========== VERIFY OTP ==========")

        request = (
            db.query(ApprovalRequest)
            .filter(
                ApprovalRequest.id == request_id
            )
            .first()
        )

        if request is None:

            print("Request Not Found")

            return None

        if request.approved:

            print("Already Approved")

            return None

        if request.expires_at < datetime.utcnow():

            print("OTP Expired")

            return None

        if request.otp != otp:

            print("Invalid OTP")

            return None

        request.approved = True

        db.commit()
        db.refresh(request)

        print("OTP Verified Successfully")
        print("===============================\n")

        return request


approval_service = ApprovalService()