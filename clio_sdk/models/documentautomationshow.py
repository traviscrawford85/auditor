from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentautomationShowIn(BaseModel):
    data: Documentautomation

class DocumentautomationShowOut(BaseModel):
    data: Documentautomation

class DocumentautomationShowUpdate(BaseModel):
    data: Documentautomation

class DocumentautomationShowDb(BaseModel):
    data: Documentautomation

