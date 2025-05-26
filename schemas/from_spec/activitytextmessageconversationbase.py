from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitytextmessageconversationBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

class ActivitytextmessageconversationBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

class ActivitytextmessageconversationBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

class ActivitytextmessageconversationBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

