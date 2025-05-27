
from pydantic import BaseModel

from .textsnippet import TextsnippetOut


class TextsnippetShowIn(BaseModel):
    data: TextsnippetIn

class TextsnippetShowOut(BaseModel):
    data: TextsnippetOut

class TextsnippetShowUpdate(BaseModel):
    data: TextsnippetUpdate

class TextsnippetShowDb(BaseModel):
    data: TextsnippetDb

