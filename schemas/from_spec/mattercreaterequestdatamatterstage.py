from typing import Optional

from pydantic import BaseModel


class MattercreaterequestdatamatterstageIn(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatamatterstageOut(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatamatterstageUpdate(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatamatterstageDb(BaseModel):
    id: Optional[str] = None

