from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommentListIn(BaseModel):
    data: List[Comment]

class CommentListOut(BaseModel):
    data: List[Comment]

class CommentListUpdate(BaseModel):
    data: List[Comment]

class CommentListDb(BaseModel):
    data: List[Comment]

