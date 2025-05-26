from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class FolderListIn(BaseModel):
    data: List[Folder]

class FolderListOut(BaseModel):
    data: List[Folder]

class FolderListUpdate(BaseModel):
    data: List[Folder]

class FolderListDb(BaseModel):
    data: List[Folder]

