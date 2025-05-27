from typing import Optional

from pydantic import BaseModel


class PhonenumberBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PhonenumberBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

