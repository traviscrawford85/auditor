from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JobtitleBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

class JobtitleBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

class JobtitleBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

class JobtitleBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

