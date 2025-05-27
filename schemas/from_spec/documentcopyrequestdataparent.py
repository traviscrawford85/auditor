from pydantic import BaseModel


class DocumentcopyrequestdataparentIn(BaseModel):
    id: int
    type: str

class DocumentcopyrequestdataparentOut(BaseModel):
    id: int
    type: str

class DocumentcopyrequestdataparentUpdate(BaseModel):
    id: int
    type: str

class DocumentcopyrequestdataparentDb(BaseModel):
    id: int
    type: str

