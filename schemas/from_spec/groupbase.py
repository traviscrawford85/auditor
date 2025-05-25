from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GroupbaseIn(BaseModel):
    client_connect_user: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

class GroupbaseOut(BaseModel):
    client_connect_user: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

class GroupbaseUpdate(BaseModel):
    client_connect_user: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

class GroupbaseDb(BaseModel):
    client_connect_user: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

