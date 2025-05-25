from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterupdaterequestdataclientIn(BaseModel):
    id: Optional[str] = None

class MatterupdaterequestdataclientOut(BaseModel):
    id: Optional[str] = None

class MatterupdaterequestdataclientUpdate(BaseModel):
    id: Optional[str] = None

class MatterupdaterequestdataclientDb(BaseModel):
    id: Optional[str] = None

