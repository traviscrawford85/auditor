from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommentcreaterequestdataitemIn(BaseModel):
    id: int

class CommentcreaterequestdataitemOut(BaseModel):
    id: int

class CommentcreaterequestdataitemUpdate(BaseModel):
    id: int

class CommentcreaterequestdataitemDb(BaseModel):
    id: int

