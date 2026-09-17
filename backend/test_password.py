from app.auth.password import (
    hash_password,
    verify_password
)

password = "Vinay123"

hashed = hash_password(password)

print("Original Password:")
print(password)

print("\nHashed Password:")
print(hashed)

print("\nCorrect Password Check:")
print(verify_password("Vinay123", hashed))

print("\nWrong Password Check:")
print(verify_password("Hello123", hashed))