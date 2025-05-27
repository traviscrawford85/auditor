from typing import Optional

from pydantic import BaseModel


class MyeventupdaterequestdataIn(BaseModel):
    marked_as_read: Optional[str] = None

class MyeventupdaterequestdataOut(BaseModel):
    marked_as_read: Optional[str] = None

class MyeventupdaterequestdataUpdate(BaseModel):
    marked_as_read: Optional[str] = None

class MyeventupdaterequestdataDb(BaseModel):
    marked_as_read: Optional[str] = None

