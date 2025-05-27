from typing import Optional

from pydantic import BaseModel


class MatterupdaterequestdataclientIn(BaseModel):
    id: Optional[str] = None

class MatterupdaterequestdataclientOut(BaseModel):
    id: Optional[str] = None

class MatterupdaterequestdataclientUpdate(BaseModel):
    id: Optional[str] = None

class MatterupdaterequestdataclientDb(BaseModel):
    id: Optional[str] = None

