from typing import List

from pydantic import BaseModel

from .medicalrecordsrequest import MedicalrecordsrequestOut


class MedicalrecordsrequestListIn(BaseModel):
    data: List[MedicalrecordsrequestIn]

class MedicalrecordsrequestListOut(BaseModel):
    data: List[MedicalrecordsrequestOut]

class MedicalrecordsrequestListUpdate(BaseModel):
    data: List[MedicalrecordsrequestUpdate]

class MedicalrecordsrequestListDb(BaseModel):
    data: List[MedicalrecordsrequestDb]

