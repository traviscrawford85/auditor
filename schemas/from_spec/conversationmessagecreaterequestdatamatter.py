from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationmessagecreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

