from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentListIn(BaseModel):
    data: List[Any]

class DocumentListOut(BaseModel):
    data: List[Any]

class DocumentListUpdate(BaseModel):
    data: List[Any]

class DocumentListDb(BaseModel):
    data: List[Any]

