from typing import Optional

from pydantic import BaseModel


class MedicalrecordsrequestupdaterequestdatamedicalbillsinnerpayersinnerIn(BaseModel):
    amount: Optional[str] = None
    holder_id: Optional[str] = None
    mark_as_lien: Optional[str] = None

class MedicalrecordsrequestupdaterequestdatamedicalbillsinnerpayersinnerOut(BaseModel):
    amount: Optional[str] = None
    holder_id: Optional[str] = None
    mark_as_lien: Optional[str] = None

class MedicalrecordsrequestupdaterequestdatamedicalbillsinnerpayersinnerUpdate(BaseModel):
    amount: Optional[str] = None
    holder_id: Optional[str] = None
    mark_as_lien: Optional[str] = None

class MedicalrecordsrequestupdaterequestdatamedicalbillsinnerpayersinnerDb(BaseModel):
    amount: Optional[str] = None
    holder_id: Optional[str] = None
    mark_as_lien: Optional[str] = None

