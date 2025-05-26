# Adapter for mattershow
from clio_sdk.models.mattershow import MattershowIn, MattershowOut, MattershowUpdate, MattershowDb
from clio_client.models.matter_show import MatterShow

def convert_sdk_to_mattershowout(src: MatterShow) -> MattershowOut:
    """Converts a clio_client model to clio_sdk model."""
    return MattershowOut(**src.model_dump())

def convert_mattershowin_to_sdk(src: MattershowIn) -> MatterShow:
    """Converts a clio_sdk model to clio_client model."""
    return MatterShow(**src.model_dump())
