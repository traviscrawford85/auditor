# Adapter for conversationmembershipbase
from clio_sdk.models.conversationmembershipbase import ConversationmembershipBaseIn, ConversationmembershipbaseOut, ConversationmembershipbaseUpdate, ConversationmembershipbaseDb
from clio_client.models.conversation_membership import ConversationMembership

def convert_sdk_to_conversationmembershipbaseout(src: ConversationMembership) -> ConversationmembershipbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ConversationmembershipbaseOut(**src.model_dump())

def convert_conversationmembershipbasein_to_sdk(src: ConversationmembershipBaseIn) -> ConversationMembership:
    """Converts a clio_sdk model to clio_client model."""
    return ConversationMembership(**src.model_dump())
