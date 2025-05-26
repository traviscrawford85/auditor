# Adapter for conversationmembershipbase
from clio_sdk.models.conversationmembershipbase import ConversationmembershipbaseIn, ConversationmembershipbaseOut, ConversationmembershipbaseUpdate, ConversationmembershipbaseDb
from clio_client.models import conversation_membership

def convert_sdk_to_conversationmembershipbaseout(src: conversation_membership) -> ConversationmembershipbaseOut:
    return ConversationmembershipbaseOut(**src.dict())

def convert_conversationmembershipbasein_to_sdk(src: ConversationmembershipbaseIn) -> conversation_membership:
    return conversation_membership(**src.dict())
