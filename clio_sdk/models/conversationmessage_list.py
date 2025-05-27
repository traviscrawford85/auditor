from typing import List

from pydantic import BaseModel

from .conversationmessage import ConversationmessageOut


class ConversationmessageListIn(BaseModel):
    data: List[ConversationmessageIn]

class ConversationmessageListOut(BaseModel):
    data: List[ConversationmessageOut]

class ConversationmessageListUpdate(BaseModel):
    data: List[ConversationmessageUpdate]

class ConversationmessageListDb(BaseModel):
    data: List[ConversationmessageDb]

