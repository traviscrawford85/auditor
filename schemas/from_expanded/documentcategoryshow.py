from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentcategoryShowIn(BaseModel):
    data: Any

class DocumentcategoryShowOut(BaseModel):
    data: Any

class DocumentcategoryShowUpdate(BaseModel):
    data: Any

class DocumentcategoryShowDb(BaseModel):
    data: Any

