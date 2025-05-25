from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationListIn(BaseModel):
    data: List[Any]

class ConversationListOut(BaseModel):
    data: List[Any]

class ConversationListUpdate(BaseModel):
    data: List[Any]

class ConversationListDb(BaseModel):
    data: List[Any]

