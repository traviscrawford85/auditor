from typing import Optional

from pydantic import BaseModel


class CustomfieldsetcreaterequestdataIn(BaseModel):
    displayed: Optional[str] = None
    name: str
    parent_type: Optional[str] = None

class CustomfieldsetcreaterequestdataOut(BaseModel):
    displayed: Optional[str] = None
    name: str
    parent_type: Optional[str] = None

class CustomfieldsetcreaterequestdataUpdate(BaseModel):
    displayed: Optional[str] = None
    name: str
    parent_type: Optional[str] = None

class CustomfieldsetcreaterequestdataDb(BaseModel):
    displayed: Optional[str] = None
    name: str
    parent_type: Optional[str] = None

