from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MultipartheaderbaseIn(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class MultipartheaderbaseOut(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class MultipartheaderbaseUpdate(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class MultipartheaderbaseDb(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

