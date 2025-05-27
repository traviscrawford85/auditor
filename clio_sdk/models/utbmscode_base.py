from typing import Optional

from pydantic import BaseModel


class UtbmscodeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmscodeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

