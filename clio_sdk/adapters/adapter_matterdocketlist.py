# Adapter for matterdocketlist
from clio_sdk.models.matterdocketlist import MatterdocketlistIn, MatterdocketlistOut, MatterdocketlistUpdate, MatterdocketlistDb
from clio_client.models.matter_docket_list import MatterDocketList

def convert_sdk_to_matterdocketlistout(src: MatterDocketList) -> MatterdocketlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return MatterdocketlistOut(**src.model_dump())

def convert_matterdocketlistin_to_sdk(src: MatterdocketlistIn) -> MatterDocketList:
    """Converts a clio_sdk model to clio_client model."""
    return MatterDocketList(**src.model_dump())
