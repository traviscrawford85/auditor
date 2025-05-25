from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktypecreaterequestdataIn(BaseModel):
    deleted_at: Optional[str] = None
    name: str

class TasktypecreaterequestdataOut(BaseModel):
    deleted_at: Optional[str] = None
    name: str

class TasktypecreaterequestdataUpdate(BaseModel):
    deleted_at: Optional[str] = None
    name: str

class TasktypecreaterequestdataDb(BaseModel):
    deleted_at: Optional[str] = None
    name: str

