from pydantic import BaseModel


class CommentcreaterequestdataitemIn(BaseModel):
    id: int

class CommentcreaterequestdataitemOut(BaseModel):
    id: int

class CommentcreaterequestdataitemUpdate(BaseModel):
    id: int

class CommentcreaterequestdataitemDb(BaseModel):
    id: int

