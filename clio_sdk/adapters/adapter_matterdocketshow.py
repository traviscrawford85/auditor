# Adapter for matterdocketshow
from clio_sdk.models.matterdocketshow import MatterdocketshowIn, MatterdocketshowOut, MatterdocketshowUpdate, MatterdocketshowDb
from clio_client.models.matter_docket_show import MatterDocketShow

def convert_sdk_to_matterdocketshowout(src: MatterDocketShow) -> MatterdocketshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return MatterdocketshowOut(**src.model_dump())

def convert_matterdocketshowin_to_sdk(src: MatterdocketshowIn) -> MatterDocketShow:
    """Converts a clio_sdk model to clio_client model."""
    return MatterDocketShow(**src.model_dump())
