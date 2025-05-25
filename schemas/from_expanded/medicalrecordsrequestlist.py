from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordsrequestListIn(BaseModel):
    data: List[Any]

class MedicalrecordsrequestListOut(BaseModel):
    data: List[Any]

class MedicalrecordsrequestListUpdate(BaseModel):
    data: List[Any]

class MedicalrecordsrequestListDb(BaseModel):
    data: List[Any]

