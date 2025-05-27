from typing import Optional

from pydantic import BaseModel


class ReportpresetBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    options: Optional[str] = None

class ReportpresetBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    options: Optional[str] = None

class ReportpresetBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    options: Optional[str] = None

class ReportpresetBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    options: Optional[str] = None

