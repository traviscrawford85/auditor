from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentShowIn(BaseModel):
    data: Any

class DocumentShowOut(BaseModel):
    data: Any

class DocumentShowUpdate(BaseModel):
    data: Any

class DocumentShowDb(BaseModel):
    data: Any

