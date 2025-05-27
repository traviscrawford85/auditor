from pydantic import BaseModel


class DocumentarchivecreaterequestdataitemsinnerIn(BaseModel):
    id: int
    type: int

class DocumentarchivecreaterequestdataitemsinnerOut(BaseModel):
    id: int
    type: int

class DocumentarchivecreaterequestdataitemsinnerUpdate(BaseModel):
    id: int
    type: int

class DocumentarchivecreaterequestdataitemsinnerDb(BaseModel):
    id: int
    type: int

