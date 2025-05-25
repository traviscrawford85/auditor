from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommentListIn(BaseModel):
    data: List[Any]

class CommentListOut(BaseModel):
    data: List[Any]

class CommentListUpdate(BaseModel):
    data: List[Any]

class CommentListDb(BaseModel):
    data: List[Any]

