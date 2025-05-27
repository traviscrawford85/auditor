from typing import Optional

from pydantic import BaseModel


class CascadingtasktemplateBaseIn(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class CascadingtasktemplateBaseOut(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class CascadingtasktemplateBaseUpdate(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class CascadingtasktemplateBaseDb(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

