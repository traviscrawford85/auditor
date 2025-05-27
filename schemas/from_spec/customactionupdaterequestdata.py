from typing import Optional

from pydantic import BaseModel


class CustomactionupdaterequestdataIn(BaseModel):
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionupdaterequestdataOut(BaseModel):
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionupdaterequestdataUpdate(BaseModel):
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionupdaterequestdataDb(BaseModel):
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

