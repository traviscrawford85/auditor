# Adapter for matterstagelist
from clio_sdk.models.matterstagelist import MatterstagelistIn, MatterstagelistOut, MatterstagelistUpdate, MatterstagelistDb
from clio_client.models import matter_stage_list

def convert_sdk_to_matterstagelistout(src: matter_stage_list) -> MatterstagelistOut:
    return MatterstagelistOut(**src.dict())

def convert_matterstagelistin_to_sdk(src: MatterstagelistIn) -> matter_stage_list:
    return matter_stage_list(**src.dict())
