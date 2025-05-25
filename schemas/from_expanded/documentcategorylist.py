from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentcategoryListIn(BaseModel):
    data: List[Any]

class DocumentcategoryListOut(BaseModel):
    data: List[Any]

class DocumentcategoryListUpdate(BaseModel):
    data: List[Any]

class DocumentcategoryListDb(BaseModel):
    data: List[Any]

