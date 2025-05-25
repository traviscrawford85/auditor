from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationShowIn(BaseModel):
    data: Any

class ConversationShowOut(BaseModel):
    data: Any

class ConversationShowUpdate(BaseModel):
    data: Any

class ConversationShowDb(BaseModel):
    data: Any

