from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommentShowIn(BaseModel):
    data: Comment

class CommentShowOut(BaseModel):
    data: Comment

class CommentShowUpdate(BaseModel):
    data: Comment

class CommentShowDb(BaseModel):
    data: Comment

