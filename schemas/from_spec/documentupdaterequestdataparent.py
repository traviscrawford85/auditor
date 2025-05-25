from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentupdaterequestdataparentIn(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class DocumentupdaterequestdataparentOut(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class DocumentupdaterequestdataparentUpdate(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class DocumentupdaterequestdataparentDb(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

