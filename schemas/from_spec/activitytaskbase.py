from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitytaskbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

class ActivitytaskbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

class ActivitytaskbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

class ActivitytaskbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None

