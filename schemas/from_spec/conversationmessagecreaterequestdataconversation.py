from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationmessagecreaterequestdataconversationIn(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdataconversationOut(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdataconversationUpdate(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdataconversationDb(BaseModel):
    id: Optional[str] = None

