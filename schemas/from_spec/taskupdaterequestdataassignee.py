from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TaskupdaterequestdataassigneeIn(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class TaskupdaterequestdataassigneeOut(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class TaskupdaterequestdataassigneeUpdate(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class TaskupdaterequestdataassigneeDb(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

