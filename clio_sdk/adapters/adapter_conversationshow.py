# Adapter for conversationshow
from clio_sdk.models.conversationshow import ConversationshowIn, ConversationshowOut, ConversationshowUpdate, ConversationshowDb
from clio_client.models import conversation_show

def convert_sdk_to_conversationshowout(src: conversation_show) -> ConversationshowOut:
    return ConversationshowOut(**src.dict())

def convert_conversationshowin_to_sdk(src: ConversationshowIn) -> conversation_show:
    return conversation_show(**src.dict())
