
from pydantic import BaseModel

from .conversationmessage import ConversationmessageOut


class ConversationmessageShowIn(BaseModel):
    data: ConversationmessageIn

class ConversationmessageShowOut(BaseModel):
    data: ConversationmessageOut

class ConversationmessageShowUpdate(BaseModel):
    data: ConversationmessageUpdate

class ConversationmessageShowDb(BaseModel):
    data: ConversationmessageDb

