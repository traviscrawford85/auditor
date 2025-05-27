from typing import Optional

from pydantic import BaseModel


class PhonenumberIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

