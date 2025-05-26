# Adapter for matterlist
from clio_sdk.models.matterlist import MatterlistIn, MatterlistOut, MatterlistUpdate, MatterlistDb
from clio_client.models.matter_list import MatterList

def convert_sdk_to_matterlistout(src: MatterList) -> MatterlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return MatterlistOut(**src.model_dump())

def convert_matterlistin_to_sdk(src: MatterlistIn) -> MatterList:
    """Converts a clio_sdk model to clio_client model."""
    return MatterList(**src.model_dump())
