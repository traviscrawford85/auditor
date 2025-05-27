from typing import Optional

from pydantic import BaseModel


class LineitemupdaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class LineitemupdaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

