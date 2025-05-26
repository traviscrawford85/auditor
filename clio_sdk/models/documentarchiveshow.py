from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentarchiveShowIn(BaseModel):
    data: Documentarchive

class DocumentarchiveShowOut(BaseModel):
    data: Documentarchive

class DocumentarchiveShowUpdate(BaseModel):
    data: Documentarchive

class DocumentarchiveShowDb(BaseModel):
    data: Documentarchive

