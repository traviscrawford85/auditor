from typing import Optional

from pydantic import BaseModel


class CustomfieldsetupdaterequestdataIn(BaseModel):
    displayed: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None

class CustomfieldsetupdaterequestdataOut(BaseModel):
    displayed: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None

class CustomfieldsetupdaterequestdataUpdate(BaseModel):
    displayed: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None

class CustomfieldsetupdaterequestdataDb(BaseModel):
    displayed: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None

