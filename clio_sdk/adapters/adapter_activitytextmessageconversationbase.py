# Adapter for activitytextmessageconversationbase
from clio_sdk.models.activitytextmessageconversationbase import ActivitytextmessageconversationBaseIn, ActivitytextmessageconversationbaseOut, ActivitytextmessageconversationbaseUpdate, ActivitytextmessageconversationbaseDb
from clio_client.models.activity_text_message_conversation import ActivityTextMessageConversation

def convert_sdk_to_activitytextmessageconversationbaseout(src: ActivityTextMessageConversation) -> ActivitytextmessageconversationbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivitytextmessageconversationbaseOut(**src.model_dump())

def convert_activitytextmessageconversationbasein_to_sdk(src: ActivitytextmessageconversationBaseIn) -> ActivityTextMessageConversation:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityTextMessageConversation(**src.model_dump())
