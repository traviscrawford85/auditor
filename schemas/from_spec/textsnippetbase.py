from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TextsnippetbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[str] = None

class TextsnippetbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[str] = None

class TextsnippetbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[str] = None

class TextsnippetbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[str] = None

