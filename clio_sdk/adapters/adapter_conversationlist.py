# Adapter for conversationlist
from clio_sdk.models.conversationlist import ConversationlistIn, ConversationlistOut, ConversationlistUpdate, ConversationlistDb
from clio_client.models import conversation_list

def convert_sdk_to_conversationlistout(src: conversation_list) -> ConversationlistOut:
    return ConversationlistOut(**src.dict())

def convert_conversationlistin_to_sdk(src: ConversationlistIn) -> conversation_list:
    return conversation_list(**src.dict())
