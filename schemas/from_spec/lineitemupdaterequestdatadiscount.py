from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LineitemupdaterequestdatadiscountIn(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None

class LineitemupdaterequestdatadiscountOut(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None

class LineitemupdaterequestdatadiscountUpdate(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None

class LineitemupdaterequestdatadiscountDb(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None

