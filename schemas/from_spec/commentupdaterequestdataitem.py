from typing import Optional

from pydantic import BaseModel


class CommentupdaterequestdataitemIn(BaseModel):
    id: Optional[str] = None

class CommentupdaterequestdataitemOut(BaseModel):
    id: Optional[str] = None

class CommentupdaterequestdataitemUpdate(BaseModel):
    id: Optional[str] = None

class CommentupdaterequestdataitemDb(BaseModel):
    id: Optional[str] = None

