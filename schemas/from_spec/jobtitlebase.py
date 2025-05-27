from typing import Optional

from pydantic import BaseModel


class JobtitleBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

class JobtitleBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

class JobtitleBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

class JobtitleBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    initials: Optional[str] = None

