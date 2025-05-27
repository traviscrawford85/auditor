from typing import Optional

from pydantic import BaseModel


class MedicalbillupdaterequestdatapayersinnerIn(BaseModel):
    amount: Optional[str] = None
    holder_id: Optional[str] = None
    mark_as_lien: Optional[str] = None

class MedicalbillupdaterequestdatapayersinnerOut(BaseModel):
    amount: Optional[str] = None
    holder_id: Optional[str] = None
    mark_as_lien: Optional[str] = None

class MedicalbillupdaterequestdatapayersinnerUpdate(BaseModel):
    amount: Optional[str] = None
    holder_id: Optional[str] = None
    mark_as_lien: Optional[str] = None

class MedicalbillupdaterequestdatapayersinnerDb(BaseModel):
    amount: Optional[str] = None
    holder_id: Optional[str] = None
    mark_as_lien: Optional[str] = None

