from datetime import datetime, timedelta
from jose import JWTError, jwt

# ==========================
# JWT Configuration
# ==========================

SECRET_KEY = "ULEDA_SECRET_KEY_2026_CHANGE_THIS_IN_PRODUCTION"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


# ==========================
# Create JWT Token
# ==========================

def create_access_token(data: dict):
    """
    Generate a JWT access token.
    """

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {
            "exp": expire
        }
    )

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# ==========================
# Verify JWT Token
# ==========================

def verify_access_token(token: str):
    """
    Verify JWT token.
    """

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        return None