from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PhonenumberBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

