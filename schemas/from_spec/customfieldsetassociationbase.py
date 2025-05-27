from typing import Optional

from pydantic import BaseModel


class CustomfieldsetassociationBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    display_order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetassociationBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    display_order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetassociationBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    display_order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetassociationBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    display_order: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

