from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationShowIn(BaseModel):
    data: Conversation

class ConversationShowOut(BaseModel):
    data: Conversation

class ConversationShowUpdate(BaseModel):
    data: Conversation

class ConversationShowDb(BaseModel):
    data: Conversation

