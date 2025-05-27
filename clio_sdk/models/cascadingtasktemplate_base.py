from typing import Optional

from pydantic import BaseModel


class CascadingtasktemplateBaseIn(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

class CascadingtasktemplateBaseOut(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

class CascadingtasktemplateBaseUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

class CascadingtasktemplateBaseDb(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

