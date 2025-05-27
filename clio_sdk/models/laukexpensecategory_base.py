from typing import Optional

from pydantic import BaseModel


class LaukexpensecategoryBaseIn(BaseModel):
    certificated: Optional[bool] = None
    civil: Optional[bool] = None
    created_at: Optional[str] = None
    criminal: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[float] = None
    updated_at: Optional[str] = None

class LaukexpensecategoryBaseOut(BaseModel):
    certificated: Optional[bool] = None
    civil: Optional[bool] = None
    created_at: Optional[str] = None
    criminal: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[float] = None
    updated_at: Optional[str] = None

class LaukexpensecategoryBaseUpdate(BaseModel):
    certificated: Optional[bool] = None
    civil: Optional[bool] = None
    created_at: Optional[str] = None
    criminal: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[float] = None
    updated_at: Optional[str] = None

class LaukexpensecategoryBaseDb(BaseModel):
    certificated: Optional[bool] = None
    civil: Optional[bool] = None
    created_at: Optional[str] = None
    criminal: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[float] = None
    updated_at: Optional[str] = None

