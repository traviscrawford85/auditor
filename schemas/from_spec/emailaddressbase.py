from typing import Optional

from pydantic import BaseModel


class EmailaddressBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class EmailaddressBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class EmailaddressBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class EmailaddressBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

