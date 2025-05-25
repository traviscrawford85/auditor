from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RemindercreaterequestdatasubjectIn(BaseModel):
    id: int
    type: str

class RemindercreaterequestdatasubjectOut(BaseModel):
    id: int
    type: str

class RemindercreaterequestdatasubjectUpdate(BaseModel):
    id: int
    type: str

class RemindercreaterequestdatasubjectDb(BaseModel):
    id: int
    type: str

