from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from app.database.connection import Base


class ApprovalRequest(Base):
    __tablename__ = "approval_requests"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)

    database_name = Column(String(255), nullable=False)

    question = Column(Text, nullable=False)

    sql_query = Column(Text, nullable=False)

    query_type = Column(String(30), nullable=False)

    otp = Column(String(6), nullable=False)

    status = Column(String(20), default="Pending")

    approved = Column(Boolean, default=False)

    attempts = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)

    expires_at = Column(DateTime, nullable=False)

    approved_at = Column(DateTime)

    approved_by = Column(String(255))