from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationmessageShowIn(BaseModel):
    data: Conversationmessage

class ConversationmessageShowOut(BaseModel):
    data: Conversationmessage

class ConversationmessageShowUpdate(BaseModel):
    data: Conversationmessage

class ConversationmessageShowDb(BaseModel):
    data: Conversationmessage

