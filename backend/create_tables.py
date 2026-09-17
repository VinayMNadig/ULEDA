from app.database.connection import Base, engine

# Import all models
from app.models.user import User
from app.models.chat import Chat
from app.models.approval_request import ApprovalRequest
from app.models.audit_log import AuditLog

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully.")