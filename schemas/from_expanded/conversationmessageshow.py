from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationmessageShowIn(BaseModel):
    data: Any

class ConversationmessageShowOut(BaseModel):
    data: Any

class ConversationmessageShowUpdate(BaseModel):
    data: Any

class ConversationmessageShowDb(BaseModel):
    data: Any

