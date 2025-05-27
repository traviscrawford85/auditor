from typing import Optional

from pydantic import BaseModel


class AccountBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class AccountBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class AccountBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class AccountBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

