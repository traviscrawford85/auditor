from typing import Optional

from pydantic import BaseModel


class TextsnippetBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[bool] = None

class TextsnippetBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[bool] = None

class TextsnippetBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[bool] = None

class TextsnippetBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[bool] = None

