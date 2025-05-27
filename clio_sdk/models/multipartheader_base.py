from typing import Optional

from pydantic import BaseModel


class MultipartheaderBaseIn(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class MultipartheaderBaseOut(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class MultipartheaderBaseUpdate(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class MultipartheaderBaseDb(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

