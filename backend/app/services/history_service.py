from sqlalchemy.orm import Session

from app.models.chat import Chat


# ==========================================
# Create Chat
# ==========================================

def create_chat(
    db: Session,
    user_id: int,
    title: str,
    messages: list,
):

    chat = Chat(
        user_id=user_id,
        title=title,
        messages=messages
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return {
        "success": True,
        "message": "Chat created successfully.",
        "chat": chat
    }


# ==========================================
# Get All Chats of User
# ==========================================

def get_user_chats(
    db: Session,
    user_id: int,
):

    chats = (
        db.query(Chat)
        .filter(Chat.user_id == user_id)
        .order_by(Chat.id.desc())
        .all()
    )

    return chats


# ==========================================
# Get Single Chat
# ==========================================

def get_chat(
    db: Session,
    chat_id: int,
):

    chat = (
        db.query(Chat)
        .filter(Chat.id == chat_id)
        .first()
    )

    if chat is None:

        return {
            "success": False,
            "message": "Chat not found."
        }

    return chat


# ==========================================
# Update Chat
# ==========================================

def update_chat(
    db: Session,
    chat_id: int,
    title: str,
    messages: list,
):

    chat = (
        db.query(Chat)
        .filter(Chat.id == chat_id)
        .first()
    )

    if chat is None:

        return {
            "success": False,
            "message": "Chat not found."
        }

    chat.title = title
    chat.messages = messages

    db.commit()
    db.refresh(chat)

    return {
        "success": True,
        "message": "Chat updated successfully.",
        "chat": chat
    }


# ==========================================
# Delete Chat
# ==========================================

def delete_chat(
    db: Session,
    chat_id: int,
):

    chat = (
        db.query(Chat)
        .filter(Chat.id == chat_id)
        .first()
    )

    if chat is None:
        return False

    db.delete(chat)
    db.commit()

    return True