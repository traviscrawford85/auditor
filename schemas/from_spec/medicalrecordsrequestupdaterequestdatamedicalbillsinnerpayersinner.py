from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

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

