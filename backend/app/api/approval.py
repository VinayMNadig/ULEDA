from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database.connection import SessionLocal
from app.database.connection_manager import connection_manager

from app.models.audit_log import AuditLog
from app.services.approval_service import approval_service
from app.services.sql_executor import execute_multi

router = APIRouter(
    prefix="/approval",
    tags=["Approval"],
)


# ==========================================
# Database Dependency
# ==========================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ==========================================
# Request Approval
# ==========================================

@router.post("/request")
def request_approval(
    request: dict,
    db: Session = Depends(get_db),
):

    question = request.get("question")
    sql = request.get("sql")
    email = request.get("email")

    if not question or not sql or not email:

        raise HTTPException(
            status_code=400,
            detail="question, sql and email are required."
        )

    approval = approval_service.create_request(

        db=db,

        question=question,

        sql=sql,

        email=email,

    )

    return {

        "success": True,

        "message": "OTP sent successfully.",

        "request_id": approval.id,

        "email": approval.approved_by,

    }


# ==========================================
# Verify OTP
# ==========================================

@router.post("/verify")
def verify_otp(
    request: dict,
    db: Session = Depends(get_db),
):

    request_id = request.get("request_id")
    otp = request.get("otp")

    if request_id is None or otp is None:

        raise HTTPException(
            status_code=400,
            detail="request_id and otp required."
        )

    approval = approval_service.verify_otp(

        db=db,

        request_id=request_id,

        otp=otp,

    )

    if approval is None:

        raise HTTPException(
            status_code=400,
            detail="Invalid OTP or expired OTP."
        )

    session = connection_manager.get_session()

    try:

        print("\n========== VERIFY OTP ==========")
        print("Question :", approval.question)
        print("SQL      :", approval.sql_query)
        print("Type     :", approval.query_type)
        print("================================\n")

        result, total_rowcount = execute_multi(
            session,
            approval.sql_query
        )

        session.commit()
                # ======================================
        # Audit Log Success
        # ======================================

        audit = AuditLog(

            question=approval.question,

            sql=approval.sql_query,

            action="EXECUTE",

            status="SUCCESS",

            executed_by=approval.approved_by,

        )

        db.add(audit)

        db.commit()

        # ======================================
        # SELECT Query
        # ======================================

        if approval.query_type == "SELECT":

            rows = result.fetchall()

            columns = result.keys()

            data = [

                dict(zip(columns, row))

                for row in rows

            ]

            return {

                "success": True,

                "message": "OTP verified successfully.",

                "answer": f"Found {len(data)} record(s).",

                "sql": approval.sql_query,

                "data": data,

                "query_type": approval.query_type,

            }

        # ======================================
        # INSERT / UPDATE / DELETE / CREATE
        # ======================================

        if approval.query_type in ["UPDATE", "DELETE"] and total_rowcount == 0:

            answer = (
                f"⚠️ {approval.query_type} ran successfully but matched 0 rows — "
                f"nothing was actually changed. The condition may not "
                f"match any existing record."
            )

        else:

            answer = f"{approval.query_type} executed successfully ({total_rowcount} row(s) affected)."

        return {

            "success": True,

            "message": "OTP verified successfully.",

            "answer": answer,

            "sql": approval.sql_query,

            "affected_rows": total_rowcount,

            "query_type": approval.query_type,

            "data": []

        }
    except Exception as e:

        import traceback

        print("\n========================================")
        print("DATABASE EXECUTION FAILED")
        print("========================================")

        traceback.print_exc()

        print("\nException:")
        print(repr(e))

        session.rollback()

        # ======================================
        # Audit Log Failure
        # ======================================

        try:

            audit = AuditLog(

                question=approval.question,

                sql=approval.sql_query,

                action="EXECUTE",

                status="FAILED",

                executed_by=approval.approved_by,

            )

            db.add(audit)

            db.commit()

        except Exception as audit_error:

            db.rollback()

            print("\nAUDIT LOG FAILED")
            print(repr(audit_error))

        # ======================================
        # Friendly Error Messages
        # ======================================

        error_message = str(e)

        if "duplicate column name" in error_message.lower():

            answer = "❌ Column already exists."

        elif "already exists" in error_message.lower():

            answer = "❌ Object already exists."

        elif "no such table" in error_message.lower():

            answer = "❌ Table not found."

        elif "no such column" in error_message.lower():

            answer = "❌ Column not found."

        elif "unique constraint failed" in error_message.lower():

            answer = "❌ Duplicate value already exists."

        elif "foreign key constraint failed" in error_message.lower():

            answer = "❌ Foreign key constraint failed."

        elif "syntax error" in error_message.lower():

            answer = "❌ Invalid SQL generated."

        else:

            answer = "❌ Database operation failed."

        return {

            "success": False,

            "message": "Execution Failed",

            "answer": answer,

            "reason": error_message,

            "sql": approval.sql_query,

            "query_type": approval.query_type,

            "data": []

        }
    finally:

        session.close()