# Adapter for mattercustomratebase
from clio_sdk.models.mattercustomratebase import MattercustomrateBaseIn, MattercustomratebaseOut, MattercustomratebaseUpdate, MattercustomratebaseDb
from clio_client.models.matter_custom_rate import MatterCustomRate

def convert_sdk_to_mattercustomratebaseout(src: MatterCustomRate) -> MattercustomratebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MattercustomratebaseOut(**src.model_dump())

def convert_mattercustomratebasein_to_sdk(src: MattercustomrateBaseIn) -> MatterCustomRate:
    """Converts a clio_sdk model to clio_client model."""
    return MatterCustomRate(**src.model_dump())
