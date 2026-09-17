from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.schema.chat_schema import (
    ChatCreate,
    ChatUpdate,
)
from app.services.chat_history_service import (
    create_chat,
    get_user_chats,
    get_chat,
    update_chat,
    delete_chat,
)

router = APIRouter(
    prefix="/chat-history",
    tags=["Chat History"],
)


# ======================================
# Database Dependency
# ======================================

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


# ======================================
# Create Chat
# ======================================

@router.post("/")
async def create_chat_api(
    request: ChatCreate,
    db: Session = Depends(get_db),
):

    print("\n========== CREATE CHAT ==========")
    print(request)
    print("=================================\n")

    return create_chat(
        db,
        request.user_id,
        request.title,
        [msg.model_dump() for msg in request.messages],
    )


# ======================================
# Get User Chats
# ======================================

@router.get("/{user_id}")
async def get_user_chat_api(
    user_id: int,
    db: Session = Depends(get_db),
):

    return get_user_chats(
        db,
        user_id,
    )


# ======================================
# Get Single Chat
# ======================================

@router.get("/single/{chat_id}")
async def get_single_chat(
    chat_id: int,
    db: Session = Depends(get_db),
):

    return get_chat(
        db,
        chat_id,
    )


# ======================================
# Update Chat
# ======================================

@router.put("/{chat_id}")
async def update_chat_api(
    chat_id: int,
    request: ChatUpdate,
    db: Session = Depends(get_db),
):

    print("\n========== UPDATE CHAT ==========")
    print("Chat ID :", chat_id)
    print("Title   :", request.title)
    print("Messages:")
    print(request.messages)
    print("=================================\n")

    return update_chat(
        db,
        chat_id,
        request.title,
        [msg.model_dump() for msg in request.messages],
    )


# ======================================
# Delete Chat
# ======================================

@router.delete("/{chat_id}")
async def delete_chat_api(
    chat_id: int,
    db: Session = Depends(get_db),
):

    return {
        "success": delete_chat(
            db,
            chat_id,
        )
    }