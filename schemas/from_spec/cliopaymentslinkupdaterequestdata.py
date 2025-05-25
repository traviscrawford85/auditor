from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CliopaymentslinkupdaterequestdataIn(BaseModel):
    expired: Optional[str] = None

class CliopaymentslinkupdaterequestdataOut(BaseModel):
    expired: Optional[str] = None

class CliopaymentslinkupdaterequestdataUpdate(BaseModel):
    expired: Optional[str] = None

class CliopaymentslinkupdaterequestdataDb(BaseModel):
    expired: Optional[str] = None

