# Adapter for matterbase
from clio_sdk.models.matterbase import MatterBaseIn, MatterbaseOut, MatterbaseUpdate, MatterbaseDb
from clio_client.models.matter import Matter

def convert_sdk_to_matterbaseout(src: Matter) -> MatterbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MatterbaseOut(**src.model_dump())

def convert_matterbasein_to_sdk(src: MatterBaseIn) -> Matter:
    """Converts a clio_sdk model to clio_client model."""
    return Matter(**src.model_dump())
