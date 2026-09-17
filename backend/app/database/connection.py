from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
)

# ==========================
# Database Path
# ==========================

BASE_DIR = Path(__file__).resolve().parents[3]

DATABASE_PATH = (
    BASE_DIR /
    "sample_database" /
    "company.db"
)

DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# ==========================
# Engine
# ==========================

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    },
    echo=True,
)

# ==========================
# Session
# ==========================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# ==========================
# Base
# ==========================

Base = declarative_base()

print("Database Path:", DATABASE_PATH)
# ==========================
# Import Models
# ==========================

from app.models.user import User
from app.models.chat import Chat
from app.models.approval_request import ApprovalRequest
from app.models.audit_log import AuditLog