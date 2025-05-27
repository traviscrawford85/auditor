from typing import List

from pydantic import BaseModel

from .comment import CommentOut


class CommentListIn(BaseModel):
    data: List[CommentIn]

class CommentListOut(BaseModel):
    data: List[CommentOut]

class CommentListUpdate(BaseModel):
    data: List[CommentUpdate]

class CommentListDb(BaseModel):
    data: List[CommentDb]

