from pydantic import BaseModel


class ConversationmessagecreaterequestdatareceiversinnerIn(BaseModel):
    id: int
    type: str

class ConversationmessagecreaterequestdatareceiversinnerOut(BaseModel):
    id: int
    type: str

class ConversationmessagecreaterequestdatareceiversinnerUpdate(BaseModel):
    id: int
    type: str

class ConversationmessagecreaterequestdatareceiversinnerDb(BaseModel):
    id: int
    type: str

