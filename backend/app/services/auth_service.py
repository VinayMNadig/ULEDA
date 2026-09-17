from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.auth.password import (
    hash_password,
    verify_password,
)
from app.auth.jwt_handler import (
    create_access_token,
)


# ==========================
# Register User
# ==========================

def register_user(
    db: Session,
    name: str,
    email: str,
    password: str,
):
    """
    Register a new user.
    """

    existing_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing_user:
        return {
            "success": False,
            "message": "Email already exists."
        }

    new_user = User(
        name=name,
        email=email,
        password=hash_password(password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "success": True,
        "message": "Registration Successful."
    }


# ==========================
# Login User
# ==========================

def login_user(
    db: Session,
    email: str,
    password: str,
):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    if not verify_password(
        password,
        user.password,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    token = create_access_token(
        {
            "user_id": user.id,
            "email": user.email,
            "role": user.role,
        }
    )

    return {
        "success": True,
        "message": "Login Successful.",
        "access_token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
        },
    }