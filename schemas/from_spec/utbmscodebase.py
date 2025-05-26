from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UtbmscodeBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodeBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodeBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodeBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

