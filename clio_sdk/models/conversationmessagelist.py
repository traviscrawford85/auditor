from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationmessageListIn(BaseModel):
    data: List[Conversationmessage]

class ConversationmessageListOut(BaseModel):
    data: List[Conversationmessage]

class ConversationmessageListUpdate(BaseModel):
    data: List[Conversationmessage]

class ConversationmessageListDb(BaseModel):
    data: List[Conversationmessage]

