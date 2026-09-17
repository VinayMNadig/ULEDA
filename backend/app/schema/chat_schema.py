from pydantic import BaseModel
from typing import List, Optional


class Message(BaseModel):
    sender: str
    text: str
    sql: Optional[str] = None
    data: Optional[list] = None


class ChatCreate(BaseModel):
    user_id: int
    title: str
    messages: List[Message]


class ChatUpdate(BaseModel):
    title: str
    messages: List[Message]


class ChatResponse(BaseModel):
    id: int
    user_id: int
    title: str
    messages: List[Message]

    class Config:
        from_attributes = True