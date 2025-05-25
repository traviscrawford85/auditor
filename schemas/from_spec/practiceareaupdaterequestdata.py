from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PracticeareaupdaterequestdataIn(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = None

class PracticeareaupdaterequestdataOut(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = None

class PracticeareaupdaterequestdataUpdate(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = None

class PracticeareaupdaterequestdataDb(BaseModel):
    category: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = None

