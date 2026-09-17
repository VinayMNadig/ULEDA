from app.database.connection import engine, Base

# Import all models
from app.models.user import User
from app.models.chat import Chat

Base.metadata.create_all(bind=engine)

print("✅ Tables Created Successfully")