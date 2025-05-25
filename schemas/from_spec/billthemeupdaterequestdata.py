from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillthemeupdaterequestdataIn(BaseModel):
    config: Optional[str] = None
    name: Optional[str] = None

class BillthemeupdaterequestdataOut(BaseModel):
    config: Optional[str] = None
    name: Optional[str] = None

class BillthemeupdaterequestdataUpdate(BaseModel):
    config: Optional[str] = None
    name: Optional[str] = None

class BillthemeupdaterequestdataDb(BaseModel):
    config: Optional[str] = None
    name: Optional[str] = None

