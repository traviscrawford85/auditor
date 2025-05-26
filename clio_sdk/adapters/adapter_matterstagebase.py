# Adapter for matterstagebase
from clio_sdk.models.matterstagebase import MatterstagebaseIn, MatterstagebaseOut, MatterstagebaseUpdate, MatterstagebaseDb
from clio_client.models import matter_stage

def convert_sdk_to_matterstagebaseout(src: matter_stage) -> MatterstagebaseOut:
    return MatterstagebaseOut(**src.dict())

def convert_matterstagebasein_to_sdk(src: MatterstagebaseIn) -> matter_stage:
    return matter_stage(**src.dict())
