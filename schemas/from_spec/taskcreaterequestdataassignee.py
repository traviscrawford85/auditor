from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TaskcreaterequestdataassigneeIn(BaseModel):
    id: int
    type: str

class TaskcreaterequestdataassigneeOut(BaseModel):
    id: int
    type: str

class TaskcreaterequestdataassigneeUpdate(BaseModel):
    id: int
    type: str

class TaskcreaterequestdataassigneeDb(BaseModel):
    id: int
    type: str

