# Adapter for conversationshow
from clio_sdk.models.conversationshow import ConversationshowIn, ConversationshowOut, ConversationshowUpdate, ConversationshowDb
from clio_client.models.conversation_show import ConversationShow

def convert_sdk_to_conversationshowout(src: ConversationShow) -> ConversationshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ConversationshowOut(**src.model_dump())

def convert_conversationshowin_to_sdk(src: ConversationshowIn) -> ConversationShow:
    """Converts a clio_sdk model to clio_client model."""
    return ConversationShow(**src.model_dump())
