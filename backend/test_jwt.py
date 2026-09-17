from app.auth.jwt_handler import (
    create_access_token,
    verify_access_token
)

token = create_access_token(
    {
        "user_id": 1,
        "email": "vinay@gmail.com",
        "role": "admin"
    }
)

print("Generated Token:\n")

print(token)

print("\nDecoded Token:\n")

print(
    verify_access_token(token)
)