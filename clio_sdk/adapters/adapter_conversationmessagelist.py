# Adapter for conversationmessagelist
from clio_sdk.models.conversationmessagelist import ConversationmessagelistIn, ConversationmessagelistOut, ConversationmessagelistUpdate, ConversationmessagelistDb
from clio_client.models.conversation_message_list import ConversationMessageList

def convert_sdk_to_conversationmessagelistout(src: ConversationMessageList) -> ConversationmessagelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ConversationmessagelistOut(**src.model_dump())

def convert_conversationmessagelistin_to_sdk(src: ConversationmessagelistIn) -> ConversationMessageList:
    """Converts a clio_sdk model to clio_client model."""
    return ConversationMessageList(**src.model_dump())
