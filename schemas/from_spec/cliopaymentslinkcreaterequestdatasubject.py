from pydantic import BaseModel


class CliopaymentslinkcreaterequestdatasubjectIn(BaseModel):
    id: int
    type: str

class CliopaymentslinkcreaterequestdatasubjectOut(BaseModel):
    id: int
    type: str

class CliopaymentslinkcreaterequestdatasubjectUpdate(BaseModel):
    id: int
    type: str

class CliopaymentslinkcreaterequestdatasubjectDb(BaseModel):
    id: int
    type: str

