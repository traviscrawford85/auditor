from typing import Optional

from pydantic import BaseModel


class PolymorphiccustomrategroupBaseIn(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrategroupBaseOut(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrategroupBaseUpdate(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class PolymorphiccustomrategroupBaseDb(BaseModel):
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

