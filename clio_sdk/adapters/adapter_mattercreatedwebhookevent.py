# Adapter for mattercreatedwebhookevent
from clio_sdk.models.mattercreatedwebhookevent import MattercreatedwebhookeventIn, MattercreatedwebhookeventOut, MattercreatedwebhookeventUpdate, MattercreatedwebhookeventDb
from clio_client.models import matter_created_webhook_event

def convert_sdk_to_mattercreatedwebhookeventout(src: matter_created_webhook_event) -> MattercreatedwebhookeventOut:
    return MattercreatedwebhookeventOut(**src.dict())

def convert_mattercreatedwebhookeventin_to_sdk(src: MattercreatedwebhookeventIn) -> matter_created_webhook_event:
    return matter_created_webhook_event(**src.dict())
