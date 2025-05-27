
from pydantic import BaseModel

from .comment import CommentOut


class CommentShowIn(BaseModel):
    data: CommentIn

class CommentShowOut(BaseModel):
    data: CommentOut

class CommentShowUpdate(BaseModel):
    data: CommentUpdate

class CommentShowDb(BaseModel):
    data: CommentDb

