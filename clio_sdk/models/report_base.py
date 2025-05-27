from typing import Optional

from pydantic import BaseModel


class ReportBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None

class ReportBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None

class ReportBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None

class ReportBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None

