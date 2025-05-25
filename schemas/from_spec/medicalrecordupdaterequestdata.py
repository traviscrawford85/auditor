from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordupdaterequestdataIn(BaseModel):
    end_date: Optional[str] = None
    start_date: Optional[str] = None

class MedicalrecordupdaterequestdataOut(BaseModel):
    end_date: Optional[str] = None
    start_date: Optional[str] = None

class MedicalrecordupdaterequestdataUpdate(BaseModel):
    end_date: Optional[str] = None
    start_date: Optional[str] = None

class MedicalrecordupdaterequestdataDb(BaseModel):
    end_date: Optional[str] = None
    start_date: Optional[str] = None

