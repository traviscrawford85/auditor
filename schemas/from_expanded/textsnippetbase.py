from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TextsnippetBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[bool] = None

class TextsnippetBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[bool] = None

class TextsnippetBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[bool] = None

class TextsnippetBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[bool] = None

