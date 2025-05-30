from pydantic import BaseModel


class CustomactioncreaterequestdataIn(BaseModel):
    label: str
    target_url: str
    ui_reference: str

class CustomactioncreaterequestdataOut(BaseModel):
    label: str
    target_url: str
    ui_reference: str

class CustomactioncreaterequestdataUpdate(BaseModel):
    label: str
    target_url: str
    ui_reference: str

class CustomactioncreaterequestdataDb(BaseModel):
    label: str
    target_url: str
    ui_reference: str

