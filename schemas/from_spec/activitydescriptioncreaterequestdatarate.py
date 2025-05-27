from typing import Optional

from pydantic import BaseModel


class ActivitydescriptioncreaterequestdatarateIn(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None

class ActivitydescriptioncreaterequestdatarateOut(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None

class ActivitydescriptioncreaterequestdatarateUpdate(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None

class ActivitydescriptioncreaterequestdatarateDb(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None

