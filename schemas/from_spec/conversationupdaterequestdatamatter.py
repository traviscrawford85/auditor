from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationupdaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class ConversationupdaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class ConversationupdaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class ConversationupdaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

