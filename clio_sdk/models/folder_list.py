from typing import List

from pydantic import BaseModel

from .folder import FolderOut


class FolderListIn(BaseModel):
    data: List[FolderIn]

class FolderListOut(BaseModel):
    data: List[FolderOut]

class FolderListUpdate(BaseModel):
    data: List[FolderUpdate]

class FolderListDb(BaseModel):
    data: List[FolderDb]

