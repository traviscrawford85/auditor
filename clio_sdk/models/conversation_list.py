from typing import List

from pydantic import BaseModel

from .conversation import ConversationOut


class ConversationListIn(BaseModel):
    data: List[ConversationIn]

class ConversationListOut(BaseModel):
    data: List[ConversationOut]

class ConversationListUpdate(BaseModel):
    data: List[ConversationUpdate]

class ConversationListDb(BaseModel):
    data: List[ConversationDb]

