from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class FolderListIn(BaseModel):
    data: List[Any]

class FolderListOut(BaseModel):
    data: List[Any]

class FolderListUpdate(BaseModel):
    data: List[Any]

class FolderListDb(BaseModel):
    data: List[Any]

