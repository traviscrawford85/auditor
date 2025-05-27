from typing import Optional

from pydantic import BaseModel


class PolymorphiccustomrateuserBaseIn(BaseModel):
    enabled: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateuserBaseOut(BaseModel):
    enabled: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateuserBaseUpdate(BaseModel):
    enabled: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrateuserBaseDb(BaseModel):
    enabled: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

