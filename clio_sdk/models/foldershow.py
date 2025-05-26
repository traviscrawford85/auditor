from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class FolderShowIn(BaseModel):
    data: Folder

class FolderShowOut(BaseModel):
    data: Folder

class FolderShowUpdate(BaseModel):
    data: Folder

class FolderShowDb(BaseModel):
    data: Folder

