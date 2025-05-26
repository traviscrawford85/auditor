# Adapter for matterstagelist
from clio_sdk.models.matterstagelist import MatterstagelistIn, MatterstagelistOut, MatterstagelistUpdate, MatterstagelistDb
from clio_client.models.matter_stage_list import MatterStageList

def convert_sdk_to_matterstagelistout(src: MatterStageList) -> MatterstagelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return MatterstagelistOut(**src.model_dump())

def convert_matterstagelistin_to_sdk(src: MatterstagelistIn) -> MatterStageList:
    """Converts a clio_sdk model to clio_client model."""
    return MatterStageList(**src.model_dump())
