from typing import Optional

from pydantic import BaseModel


class DocumentupdaterequestdataparentIn(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class DocumentupdaterequestdataparentOut(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class DocumentupdaterequestdataparentUpdate(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class DocumentupdaterequestdataparentDb(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

