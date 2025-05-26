from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PhonenumberBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PhonenumberBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PhonenumberBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PhonenumberBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

