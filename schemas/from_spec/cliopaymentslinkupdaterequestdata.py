from typing import Optional

from pydantic import BaseModel


class CliopaymentslinkupdaterequestdataIn(BaseModel):
    expired: Optional[str] = None

class CliopaymentslinkupdaterequestdataOut(BaseModel):
    expired: Optional[str] = None

class CliopaymentslinkupdaterequestdataUpdate(BaseModel):
    expired: Optional[str] = None

class CliopaymentslinkupdaterequestdataDb(BaseModel):
    expired: Optional[str] = None

