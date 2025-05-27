from typing import Optional

from pydantic import BaseModel


class TasktypeupdaterequestdataIn(BaseModel):
    deleted_at: Optional[str] = None
    name: Optional[str] = None

class TasktypeupdaterequestdataOut(BaseModel):
    deleted_at: Optional[str] = None
    name: Optional[str] = None

class TasktypeupdaterequestdataUpdate(BaseModel):
    deleted_at: Optional[str] = None
    name: Optional[str] = None

class TasktypeupdaterequestdataDb(BaseModel):
    deleted_at: Optional[str] = None
    name: Optional[str] = None

