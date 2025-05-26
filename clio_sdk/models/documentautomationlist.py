from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentautomationListIn(BaseModel):
    data: List[Documentautomation]

class DocumentautomationListOut(BaseModel):
    data: List[Documentautomation]

class DocumentautomationListUpdate(BaseModel):
    data: List[Documentautomation]

class DocumentautomationListDb(BaseModel):
    data: List[Documentautomation]

