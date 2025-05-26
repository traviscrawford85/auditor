# Adapter for conversationmessagelist
from clio_sdk.models.conversationmessagelist import ConversationmessagelistIn, ConversationmessagelistOut, ConversationmessagelistUpdate, ConversationmessagelistDb
from clio_client.models import conversation_message_list

def convert_sdk_to_conversationmessagelistout(src: conversation_message_list) -> ConversationmessagelistOut:
    return ConversationmessagelistOut(**src.dict())

def convert_conversationmessagelistin_to_sdk(src: ConversationmessagelistIn) -> conversation_message_list:
    return conversation_message_list(**src.dict())
