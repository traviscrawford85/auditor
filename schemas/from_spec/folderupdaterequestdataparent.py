from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class FolderupdaterequestdataparentIn(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class FolderupdaterequestdataparentOut(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class FolderupdaterequestdataparentUpdate(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class FolderupdaterequestdataparentDb(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

