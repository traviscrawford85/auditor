from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentversionListIn(BaseModel):
    data: List[Any]

class DocumentversionListOut(BaseModel):
    data: List[Any]

class DocumentversionListUpdate(BaseModel):
    data: List[Any]

class DocumentversionListDb(BaseModel):
    data: List[Any]

