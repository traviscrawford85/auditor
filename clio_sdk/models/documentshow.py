from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentShowIn(BaseModel):
    data: Document

class DocumentShowOut(BaseModel):
    data: Document

class DocumentShowUpdate(BaseModel):
    data: Document

class DocumentShowDb(BaseModel):
    data: Document

