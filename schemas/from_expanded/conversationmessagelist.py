from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationmessageListIn(BaseModel):
    data: List[Any]

class ConversationmessageListOut(BaseModel):
    data: List[Any]

class ConversationmessageListUpdate(BaseModel):
    data: List[Any]

class ConversationmessageListDb(BaseModel):
    data: List[Any]

