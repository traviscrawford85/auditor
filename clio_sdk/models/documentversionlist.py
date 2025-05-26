from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentversionListIn(BaseModel):
    data: List[Documentversion]

class DocumentversionListOut(BaseModel):
    data: List[Documentversion]

class DocumentversionListUpdate(BaseModel):
    data: List[Documentversion]

class DocumentversionListDb(BaseModel):
    data: List[Documentversion]

