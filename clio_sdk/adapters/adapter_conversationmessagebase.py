# Adapter for conversationmessagebase
from clio_sdk.models.conversationmessagebase import ConversationmessagebaseIn, ConversationmessagebaseOut, ConversationmessagebaseUpdate, ConversationmessagebaseDb
from clio_client.models import conversation_message

def convert_sdk_to_conversationmessagebaseout(src: conversation_message) -> ConversationmessagebaseOut:
    return ConversationmessagebaseOut(**src.dict())

def convert_conversationmessagebasein_to_sdk(src: ConversationmessagebaseIn) -> conversation_message:
    return conversation_message(**src.dict())
