from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentautomationListIn(BaseModel):
    data: List[Any]

class DocumentautomationListOut(BaseModel):
    data: List[Any]

class DocumentautomationListUpdate(BaseModel):
    data: List[Any]

class DocumentautomationListDb(BaseModel):
    data: List[Any]

