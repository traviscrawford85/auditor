from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LineitemupdaterequestdatabillIn(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatabillOut(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatabillUpdate(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatabillDb(BaseModel):
    id: Optional[str] = None

