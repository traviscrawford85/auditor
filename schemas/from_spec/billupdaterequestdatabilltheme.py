from typing import Optional

from pydantic import BaseModel


class BillupdaterequestdatabillthemeIn(BaseModel):
    id: Optional[str] = None

class BillupdaterequestdatabillthemeOut(BaseModel):
    id: Optional[str] = None

class BillupdaterequestdatabillthemeUpdate(BaseModel):
    id: Optional[str] = None

class BillupdaterequestdatabillthemeDb(BaseModel):
    id: Optional[str] = None

