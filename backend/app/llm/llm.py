import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# backend/.env
env_path = Path(__file__).resolve().parents[2] / ".env"

load_dotenv(dotenv_path=env_path)

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name=os.getenv("MODEL_NAME"),
    temperature=0
)