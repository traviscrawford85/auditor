# Adapter for matterstagebase
from clio_sdk.models.matterstagebase import MatterstageBaseIn, MatterstagebaseOut, MatterstagebaseUpdate, MatterstagebaseDb
from clio_client.models.matter_stage import MatterStage

def convert_sdk_to_matterstagebaseout(src: MatterStage) -> MatterstagebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MatterstagebaseOut(**src.model_dump())

def convert_matterstagebasein_to_sdk(src: MatterstageBaseIn) -> MatterStage:
    """Converts a clio_sdk model to clio_client model."""
    return MatterStage(**src.model_dump())
