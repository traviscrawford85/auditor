from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class FolderShowIn(BaseModel):
    data: Any

class FolderShowOut(BaseModel):
    data: Any

class FolderShowUpdate(BaseModel):
    data: Any

class FolderShowDb(BaseModel):
    data: Any

