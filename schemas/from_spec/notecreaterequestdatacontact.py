from pydantic import BaseModel


class NotecreaterequestdatacontactIn(BaseModel):
    id: int

class NotecreaterequestdatacontactOut(BaseModel):
    id: int

class NotecreaterequestdatacontactUpdate(BaseModel):
    id: int

class NotecreaterequestdatacontactDb(BaseModel):
    id: int

