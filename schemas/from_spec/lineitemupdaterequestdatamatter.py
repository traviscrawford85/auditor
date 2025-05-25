from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LineitemupdaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

