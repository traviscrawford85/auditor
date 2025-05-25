from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentcategoryupdaterequestdataIn(BaseModel):
    name: Optional[str] = None

class DocumentcategoryupdaterequestdataOut(BaseModel):
    name: Optional[str] = None

class DocumentcategoryupdaterequestdataUpdate(BaseModel):
    name: Optional[str] = None

class DocumentcategoryupdaterequestdataDb(BaseModel):
    name: Optional[str] = None

