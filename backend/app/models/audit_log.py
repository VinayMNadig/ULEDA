from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from app.database.connection import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)

    question = Column(Text)

    sql = Column(Text)

    action = Column(String(50))

    status = Column(String(50))

    executed_by = Column(String(255))

    executed_at = Column(DateTime, default=datetime.utcnow)