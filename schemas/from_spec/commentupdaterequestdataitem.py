from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommentupdaterequestdataitemIn(BaseModel):
    id: Optional[str] = None

class CommentupdaterequestdataitemOut(BaseModel):
    id: Optional[str] = None

class CommentupdaterequestdataitemUpdate(BaseModel):
    id: Optional[str] = None

class CommentupdaterequestdataitemDb(BaseModel):
    id: Optional[str] = None

