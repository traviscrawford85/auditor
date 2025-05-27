from typing import Optional

from pydantic import BaseModel


class MatterbillrecipientBaseIn(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    updated_at: Optional[str] = None

class MatterbillrecipientBaseOut(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    updated_at: Optional[str] = None

class MatterbillrecipientBaseUpdate(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    updated_at: Optional[str] = None

class MatterbillrecipientBaseDb(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    updated_at: Optional[str] = None

