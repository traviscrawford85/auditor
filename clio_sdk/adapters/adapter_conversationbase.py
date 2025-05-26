# Adapter for conversationbase
from clio_sdk.models.conversationbase import ConversationbaseIn, ConversationbaseOut, ConversationbaseUpdate, ConversationbaseDb
from clio_client.models import conversation

def convert_sdk_to_conversationbaseout(src: conversation) -> ConversationbaseOut:
    return ConversationbaseOut(**src.dict())

def convert_conversationbasein_to_sdk(src: ConversationbaseIn) -> conversation:
    return conversation(**src.dict())
