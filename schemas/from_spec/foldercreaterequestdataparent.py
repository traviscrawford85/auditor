from pydantic import BaseModel


class FoldercreaterequestdataparentIn(BaseModel):
    id: int
    type: str

class FoldercreaterequestdataparentOut(BaseModel):
    id: int
    type: str

class FoldercreaterequestdataparentUpdate(BaseModel):
    id: int
    type: str

class FoldercreaterequestdataparentDb(BaseModel):
    id: int
    type: str

