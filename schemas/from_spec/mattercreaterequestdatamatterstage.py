from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MattercreaterequestdatamatterstageIn(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatamatterstageOut(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatamatterstageUpdate(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatamatterstageDb(BaseModel):
    id: Optional[str] = None

