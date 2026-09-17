import json

from sqlalchemy.orm import Session

from app.models.chat import Chat


# ==========================
# Create Chat
# ==========================

def create_chat(
    db: Session,
    user_id: int,
    title: str,
    messages: list,
):

    chat = Chat(
        user_id=user_id,
        title=title,
        messages=json.dumps(messages),
    )

    db.add(chat)

    db.commit()

    db.refresh(chat)

    return chat


# ==========================
# Get All Chats
# ==========================

def get_user_chats(
    db: Session,
    user_id: int,
):

    chats = (
        db.query(Chat)
        .filter(Chat.user_id == user_id)
        .order_by(Chat.updated_at.desc())
        .all()
    )

    result = []

    for chat in chats:

        result.append({

            "id": chat.id,

            "title": chat.title,

            "messages": json.loads(chat.messages),

            "created_at": chat.created_at,

            "updated_at": chat.updated_at,

        })

    return result


# ==========================
# Get One Chat
# ==========================

def get_chat(
    db: Session,
    chat_id: int,
):

    chat = (
        db.query(Chat)
        .filter(Chat.id == chat_id)
        .first()
    )

    if not chat:

        return None

    return {

        "id": chat.id,

        "title": chat.title,

        "messages": json.loads(chat.messages),

    }


# ==========================
# Update Chat
# ==========================

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

    if not chat:

        return None

    chat.title = title

    chat.messages = json.dumps(messages)

    db.commit()

    db.refresh(chat)

    return chat


# ==========================
# Delete Chat
# ==========================

def delete_chat(
    db: Session,
    chat_id: int,
):

    chat = (
        db.query(Chat)
        .filter(Chat.id == chat_id)
        .first()
    )

    if not chat:

        return False

    db.delete(chat)

    db.commit()

    return True