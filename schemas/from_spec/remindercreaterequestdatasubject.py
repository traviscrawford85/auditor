from pydantic import BaseModel


class RemindercreaterequestdatasubjectIn(BaseModel):
    id: int
    type: str

class RemindercreaterequestdatasubjectOut(BaseModel):
    id: int
    type: str

class RemindercreaterequestdatasubjectUpdate(BaseModel):
    id: int
    type: str

class RemindercreaterequestdatasubjectDb(BaseModel):
    id: int
    type: str

