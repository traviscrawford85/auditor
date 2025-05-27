from typing import Optional

from pydantic import BaseModel


class LienBaseIn(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LienBaseOut(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LienBaseUpdate(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LienBaseDb(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    lien_type: Optional[str] = None
    mark_as_lien: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

