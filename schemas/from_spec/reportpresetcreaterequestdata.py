from pydantic import BaseModel


class ReportpresetcreaterequestdataIn(BaseModel):
    format: str
    kind: str
    name: str
    options: str

class ReportpresetcreaterequestdataOut(BaseModel):
    format: str
    kind: str
    name: str
    options: str

class ReportpresetcreaterequestdataUpdate(BaseModel):
    format: str
    kind: str
    name: str
    options: str

class ReportpresetcreaterequestdataDb(BaseModel):
    format: str
    kind: str
    name: str
    options: str

