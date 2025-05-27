from typing import Optional

from pydantic import BaseModel


class TextsnippetIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[str] = None

class TextsnippetOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[str] = None

class TextsnippetUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[str] = None

class TextsnippetDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[str] = None

