from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktypeupdaterequestdataIn(BaseModel):
    deleted_at: Optional[str] = None
    name: Optional[str] = None

class TasktypeupdaterequestdataOut(BaseModel):
    deleted_at: Optional[str] = None
    name: Optional[str] = None

class TasktypeupdaterequestdataUpdate(BaseModel):
    deleted_at: Optional[str] = None
    name: Optional[str] = None

class TasktypeupdaterequestdataDb(BaseModel):
    deleted_at: Optional[str] = None
    name: Optional[str] = None

