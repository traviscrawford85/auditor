from typing import Optional

from pydantic import BaseModel


class PolymorphiccustomrateGroupBaseIn(BaseModel):
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

class PolymorphiccustomrateGroupBaseOut(BaseModel):
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

class PolymorphiccustomrateGroupBaseUpdate(BaseModel):
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

class PolymorphiccustomrateGroupBaseDb(BaseModel):
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None

