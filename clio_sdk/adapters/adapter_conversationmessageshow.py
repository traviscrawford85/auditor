# Adapter for conversationmessageshow
from clio_sdk.models.conversationmessageshow import ConversationmessageshowIn, ConversationmessageshowOut, ConversationmessageshowUpdate, ConversationmessageshowDb
from clio_client.models.conversation_message_show import ConversationMessageShow

def convert_sdk_to_conversationmessageshowout(src: ConversationMessageShow) -> ConversationmessageshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ConversationmessageshowOut(**src.model_dump())

def convert_conversationmessageshowin_to_sdk(src: ConversationmessageshowIn) -> ConversationMessageShow:
    """Converts a clio_sdk model to clio_client model."""
    return ConversationMessageShow(**src.model_dump())
