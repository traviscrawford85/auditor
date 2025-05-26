from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UtbmscodeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UtbmscodeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UtbmscodeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UtbmscodeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

