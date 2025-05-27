from typing import Optional

from pydantic import BaseModel


class ContingencyfeeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[bool] = None

class ContingencyfeeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[bool] = None

class ContingencyfeeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[bool] = None

class ContingencyfeeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[bool] = None

