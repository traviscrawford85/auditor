from typing import Optional

from pydantic import BaseModel


class BillthemeupdaterequestdataIn(BaseModel):
    config: Optional[str] = None
    name: Optional[str] = None

class BillthemeupdaterequestdataOut(BaseModel):
    config: Optional[str] = None
    name: Optional[str] = None

class BillthemeupdaterequestdataUpdate(BaseModel):
    config: Optional[str] = None
    name: Optional[str] = None

class BillthemeupdaterequestdataDb(BaseModel):
    config: Optional[str] = None
    name: Optional[str] = None

