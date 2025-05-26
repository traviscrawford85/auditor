# Adapter for mattercreatedwebhookevent
from clio_sdk.models.mattercreatedwebhookevent import MattercreatedwebhookeventIn, MattercreatedwebhookeventOut, MattercreatedwebhookeventUpdate, MattercreatedwebhookeventDb
from clio_client.models.matter_created_webhook_event import MatterCreatedWebhookEvent

def convert_sdk_to_mattercreatedwebhookeventout(src: MatterCreatedWebhookEvent) -> MattercreatedwebhookeventOut:
    """Converts a clio_client model to clio_sdk model."""
    return MattercreatedwebhookeventOut(**src.model_dump())

def convert_mattercreatedwebhookeventin_to_sdk(src: MattercreatedwebhookeventIn) -> MatterCreatedWebhookEvent:
    """Converts a clio_sdk model to clio_client model."""
    return MatterCreatedWebhookEvent(**src.model_dump())
