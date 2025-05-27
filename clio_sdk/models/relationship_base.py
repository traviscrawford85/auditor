from typing import Optional

from pydantic import BaseModel


class RelationshipBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RelationshipBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RelationshipBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RelationshipBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

