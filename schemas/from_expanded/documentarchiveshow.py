from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentarchiveShowIn(BaseModel):
    data: Any

class DocumentarchiveShowOut(BaseModel):
    data: Any

class DocumentarchiveShowUpdate(BaseModel):
    data: Any

class DocumentarchiveShowDb(BaseModel):
    data: Any

