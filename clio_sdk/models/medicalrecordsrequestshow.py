from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordsrequestShowIn(BaseModel):
    data: Medicalrecordsrequest

class MedicalrecordsrequestShowOut(BaseModel):
    data: Medicalrecordsrequest

class MedicalrecordsrequestShowUpdate(BaseModel):
    data: Medicalrecordsrequest

class MedicalrecordsrequestShowDb(BaseModel):
    data: Medicalrecordsrequest

