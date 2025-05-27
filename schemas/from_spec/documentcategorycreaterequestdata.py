from pydantic import BaseModel


class DocumentcategorycreaterequestdataIn(BaseModel):
    name: str

class DocumentcategorycreaterequestdataOut(BaseModel):
    name: str

class DocumentcategorycreaterequestdataUpdate(BaseModel):
    name: str

class DocumentcategorycreaterequestdataDb(BaseModel):
    name: str

