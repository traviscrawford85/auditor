from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentListIn(BaseModel):
    data: List[Document]

class DocumentListOut(BaseModel):
    data: List[Document]

class DocumentListUpdate(BaseModel):
    data: List[Document]

class DocumentListDb(BaseModel):
    data: List[Document]

