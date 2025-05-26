from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordsrequestListIn(BaseModel):
    data: List[Medicalrecordsrequest]

class MedicalrecordsrequestListOut(BaseModel):
    data: List[Medicalrecordsrequest]

class MedicalrecordsrequestListUpdate(BaseModel):
    data: List[Medicalrecordsrequest]

class MedicalrecordsrequestListDb(BaseModel):
    data: List[Medicalrecordsrequest]

