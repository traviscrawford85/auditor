from typing import Optional

from pydantic import BaseModel


class MatterupdaterequestdatasplitinvoicepayersinnerIn(BaseModel):
    contact_id: Optional[str] = None
    id: Optional[str] = None
    send_to_bill_recipients: Optional[str] = None
    split_portion: Optional[str] = None
    _destroy: Optional[str] = None

class MatterupdaterequestdatasplitinvoicepayersinnerOut(BaseModel):
    contact_id: Optional[str] = None
    id: Optional[str] = None
    send_to_bill_recipients: Optional[str] = None
    split_portion: Optional[str] = None
    _destroy: Optional[str] = None

class MatterupdaterequestdatasplitinvoicepayersinnerUpdate(BaseModel):
    contact_id: Optional[str] = None
    id: Optional[str] = None
    send_to_bill_recipients: Optional[str] = None
    split_portion: Optional[str] = None
    _destroy: Optional[str] = None

class MatterupdaterequestdatasplitinvoicepayersinnerDb(BaseModel):
    contact_id: Optional[str] = None
    id: Optional[str] = None
    send_to_bill_recipients: Optional[str] = None
    split_portion: Optional[str] = None
    _destroy: Optional[str] = None

