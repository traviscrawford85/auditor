from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

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

