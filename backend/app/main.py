from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ===========================
# Database
# ===========================

from app.database.connection import Base, engine

# Import all models
from app.models.user import User
from app.models.chat import Chat
from app.models.approval_request import ApprovalRequest
from app.models.audit_log import AuditLog

# Create tables
Base.metadata.create_all(bind=engine)

# ===========================
# Routers
# ===========================

from app.api.auth_routes import router as auth_router
from app.api.chat import router as chat_router
from app.api.chat_history import router as chat_history_router
from app.api.connection import router as connection_router
from app.api.upload import router as upload_router
from app.api.schema import router as schema_router
from app.api.active_database import router as active_database_router
from app.api.approval import router as approval_router
from app.api.database_manager import router as database_manager_router

# ===========================
# FastAPI App
# ===========================

app = FastAPI(
    title="ULEDA AI Database Assistant",
    description="Universal LLM Database Assistant",
    version="2.0.0",
)

# ===========================
# CORS
# ===========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===========================
# Root
# ===========================

@app.get("/")
def root():
    return {
        "success": True,
        "application": "ULEDA",
        "version": "2.0.0",
        "message": "ULEDA Backend Running Successfully 🚀",
    }

# ===========================
# Health
# ===========================

@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "backend": "Running",
        "database": "Ready",
    }

# ===========================
# Register Routers
# ===========================

app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(chat_history_router)
app.include_router(connection_router)
app.include_router(upload_router)
app.include_router(schema_router)
app.include_router(active_database_router)
app.include_router(approval_router)
app.include_router(database_manager_router)