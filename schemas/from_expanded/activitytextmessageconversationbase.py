from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityTextmessageconversationBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

class ActivityTextmessageconversationBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

class ActivityTextmessageconversationBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

class ActivityTextmessageconversationBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

