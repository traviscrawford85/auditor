from typing import List

from pydantic import BaseModel

from .textsnippet import TextsnippetOut


class TextsnippetListIn(BaseModel):
    data: List[TextsnippetIn]

class TextsnippetListOut(BaseModel):
    data: List[TextsnippetOut]

class TextsnippetListUpdate(BaseModel):
    data: List[TextsnippetUpdate]

class TextsnippetListDb(BaseModel):
    data: List[TextsnippetDb]

