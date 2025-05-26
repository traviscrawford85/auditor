from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CliopaymentslinkShowIn(BaseModel):
    data: Cliopaymentslink

class CliopaymentslinkShowOut(BaseModel):
    data: Cliopaymentslink

class CliopaymentslinkShowUpdate(BaseModel):
    data: Cliopaymentslink

class CliopaymentslinkShowDb(BaseModel):
    data: Cliopaymentslink

