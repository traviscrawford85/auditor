from typing import Optional

from pydantic import BaseModel


class ActivityTaskBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

class ActivityTaskBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

class ActivityTaskBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

class ActivityTaskBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

