from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UtbmscodebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

