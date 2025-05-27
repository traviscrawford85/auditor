
from pydantic import BaseModel

from .folder import FolderOut


class FolderShowIn(BaseModel):
    data: FolderIn

class FolderShowOut(BaseModel):
    data: FolderOut

class FolderShowUpdate(BaseModel):
    data: FolderUpdate

class FolderShowDb(BaseModel):
    data: FolderDb

