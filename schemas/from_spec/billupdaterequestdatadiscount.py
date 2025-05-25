from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillupdaterequestdatadiscountIn(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None

class BillupdaterequestdatadiscountOut(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None

class BillupdaterequestdatadiscountUpdate(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None

class BillupdaterequestdatadiscountDb(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None

