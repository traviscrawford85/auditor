from typing import Optional

from pydantic import BaseModel


class MattercreaterequestdatasplitinvoicepayersinnerIn(BaseModel):
    contact_id: int
    send_to_bill_recipients: Optional[str] = None
    split_portion: str

class MattercreaterequestdatasplitinvoicepayersinnerOut(BaseModel):
    contact_id: int
    send_to_bill_recipients: Optional[str] = None
    split_portion: str

class MattercreaterequestdatasplitinvoicepayersinnerUpdate(BaseModel):
    contact_id: int
    send_to_bill_recipients: Optional[str] = None
    split_portion: str

class MattercreaterequestdatasplitinvoicepayersinnerDb(BaseModel):
    contact_id: int
    send_to_bill_recipients: Optional[str] = None
    split_portion: str

