from typing import Optional

from pydantic import BaseModel


class UtbmscodeIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodeOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodeUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodeDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

