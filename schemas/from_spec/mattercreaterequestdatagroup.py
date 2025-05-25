from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MattercreaterequestdatagroupIn(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatagroupOut(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatagroupUpdate(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatagroupDb(BaseModel):
    id: Optional[str] = None

