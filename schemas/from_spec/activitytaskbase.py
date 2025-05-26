from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitytaskBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

class ActivitytaskBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

class ActivitytaskBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

class ActivitytaskBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

