from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CliopaymentspaymentShowIn(BaseModel):
    data: Cliopaymentspayment

class CliopaymentspaymentShowOut(BaseModel):
    data: Cliopaymentspayment

class CliopaymentspaymentShowUpdate(BaseModel):
    data: Cliopaymentspayment

class CliopaymentspaymentShowDb(BaseModel):
    data: Cliopaymentspayment

