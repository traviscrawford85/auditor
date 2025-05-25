from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommentShowIn(BaseModel):
    data: Any

class CommentShowOut(BaseModel):
    data: Any

class CommentShowUpdate(BaseModel):
    data: Any

class CommentShowDb(BaseModel):
    data: Any

