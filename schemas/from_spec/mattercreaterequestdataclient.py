from pydantic import BaseModel


class MattercreaterequestdataclientIn(BaseModel):
    id: int

class MattercreaterequestdataclientOut(BaseModel):
    id: int

class MattercreaterequestdataclientUpdate(BaseModel):
    id: int

class MattercreaterequestdataclientDb(BaseModel):
    id: int

