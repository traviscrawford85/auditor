from typing import Optional

from pydantic import BaseModel


class DocumentarchiveBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[int] = None
    progress: Optional[float] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[int] = None
    progress: Optional[float] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[int] = None
    progress: Optional[float] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[int] = None
    progress: Optional[float] = None
    state: Optional[str] = None
    message: Optional[str] = None

