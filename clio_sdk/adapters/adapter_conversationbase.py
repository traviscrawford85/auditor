# Adapter for conversationbase
from clio_sdk.models.conversationbase import ConversationBaseIn, ConversationbaseOut, ConversationbaseUpdate, ConversationbaseDb
from clio_client.models.conversation import Conversation

def convert_sdk_to_conversationbaseout(src: Conversation) -> ConversationbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ConversationbaseOut(**src.model_dump())

def convert_conversationbasein_to_sdk(src: ConversationBaseIn) -> Conversation:
    """Converts a clio_sdk model to clio_client model."""
    return Conversation(**src.model_dump())
