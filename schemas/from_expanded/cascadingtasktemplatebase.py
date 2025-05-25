from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

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

