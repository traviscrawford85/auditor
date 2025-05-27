from pydantic import BaseModel


class NotecreaterequestdatamatterIn(BaseModel):
    id: int

class NotecreaterequestdatamatterOut(BaseModel):
    id: int

class NotecreaterequestdatamatterUpdate(BaseModel):
    id: int

class NotecreaterequestdatamatterDb(BaseModel):
    id: int

