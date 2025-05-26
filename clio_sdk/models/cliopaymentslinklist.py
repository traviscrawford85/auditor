from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CliopaymentslinkListIn(BaseModel):
    data: List[Cliopaymentslink]

class CliopaymentslinkListOut(BaseModel):
    data: List[Cliopaymentslink]

class CliopaymentslinkListUpdate(BaseModel):
    data: List[Cliopaymentslink]

class CliopaymentslinkListDb(BaseModel):
    data: List[Cliopaymentslink]

