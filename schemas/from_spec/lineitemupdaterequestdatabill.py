from typing import Optional

from pydantic import BaseModel


class LineitemupdaterequestdatabillIn(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatabillOut(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatabillUpdate(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatabillDb(BaseModel):
    id: Optional[str] = None

