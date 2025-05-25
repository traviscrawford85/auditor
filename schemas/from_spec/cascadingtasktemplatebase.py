from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CascadingtasktemplatebaseIn(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class CascadingtasktemplatebaseOut(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class CascadingtasktemplatebaseUpdate(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class CascadingtasktemplatebaseDb(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

