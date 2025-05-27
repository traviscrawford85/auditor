
from pydantic import BaseModel

from .conversation import ConversationOut


class ConversationShowIn(BaseModel):
    data: ConversationIn

class ConversationShowOut(BaseModel):
    data: ConversationOut

class ConversationShowUpdate(BaseModel):
    data: ConversationUpdate

class ConversationShowDb(BaseModel):
    data: ConversationDb

