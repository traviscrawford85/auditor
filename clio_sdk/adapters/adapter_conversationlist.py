# Adapter for conversationlist
from clio_sdk.models.conversationlist import ConversationlistIn, ConversationlistOut, ConversationlistUpdate, ConversationlistDb
from clio_client.models.conversation_list import ConversationList

def convert_sdk_to_conversationlistout(src: ConversationList) -> ConversationlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ConversationlistOut(**src.model_dump())

def convert_conversationlistin_to_sdk(src: ConversationlistIn) -> ConversationList:
    """Converts a clio_sdk model to clio_client model."""
    return ConversationList(**src.model_dump())
