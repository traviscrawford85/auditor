from typing import Optional

from pydantic import BaseModel


class CurrencyBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CurrencyBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CurrencyBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CurrencyBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

