# Adapter for matterdocketbase
from clio_sdk.models.matterdocketbase import MatterdocketBaseIn, MatterdocketbaseOut, MatterdocketbaseUpdate, MatterdocketbaseDb
from clio_client.models.matter_docket import MatterDocket

def convert_sdk_to_matterdocketbaseout(src: MatterDocket) -> MatterdocketbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MatterdocketbaseOut(**src.model_dump())

def convert_matterdocketbasein_to_sdk(src: MatterdocketBaseIn) -> MatterDocket:
    """Converts a clio_sdk model to clio_client model."""
    return MatterDocket(**src.model_dump())
