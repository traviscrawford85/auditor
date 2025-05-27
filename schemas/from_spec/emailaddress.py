from typing import Optional

from pydantic import BaseModel


class EmailaddressIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class EmailaddressOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class EmailaddressUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class EmailaddressDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

