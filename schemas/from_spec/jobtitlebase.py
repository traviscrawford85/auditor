from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JobtitlebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

class JobtitlebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

class JobtitlebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

class JobtitlebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

