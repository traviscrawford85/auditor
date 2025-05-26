# Adapter for conversationmessageshow
from clio_sdk.models.conversationmessageshow import ConversationmessageshowIn, ConversationmessageshowOut, ConversationmessageshowUpdate, ConversationmessageshowDb
from clio_client.models import conversation_message_show

def convert_sdk_to_conversationmessageshowout(src: conversation_message_show) -> ConversationmessageshowOut:
    return ConversationmessageshowOut(**src.dict())

def convert_conversationmessageshowin_to_sdk(src: ConversationmessageshowIn) -> conversation_message_show:
    return conversation_message_show(**src.dict())
