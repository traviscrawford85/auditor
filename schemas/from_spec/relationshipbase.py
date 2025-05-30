from typing import Optional

from pydantic import BaseModel


class RelationshipBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RelationshipBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RelationshipBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RelationshipBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

