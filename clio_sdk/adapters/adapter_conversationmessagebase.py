# Adapter for conversationmessagebase
from clio_sdk.models.conversationmessagebase import ConversationmessageBaseIn, ConversationmessagebaseOut, ConversationmessagebaseUpdate, ConversationmessagebaseDb
from clio_client.models.conversation_message import ConversationMessage

def convert_sdk_to_conversationmessagebaseout(src: ConversationMessage) -> ConversationmessagebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ConversationmessagebaseOut(**src.model_dump())

def convert_conversationmessagebasein_to_sdk(src: ConversationmessageBaseIn) -> ConversationMessage:
    """Converts a clio_sdk model to clio_client model."""
    return ConversationMessage(**src.model_dump())
