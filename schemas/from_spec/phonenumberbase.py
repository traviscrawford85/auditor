from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PhonenumberbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

