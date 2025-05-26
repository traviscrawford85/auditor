from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationListIn(BaseModel):
    data: List[Conversation]

class ConversationListOut(BaseModel):
    data: List[Conversation]

class ConversationListUpdate(BaseModel):
    data: List[Conversation]

class ConversationListDb(BaseModel):
    data: List[Conversation]

