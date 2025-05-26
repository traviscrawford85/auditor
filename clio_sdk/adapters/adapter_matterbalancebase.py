# Adapter for matterbalancebase
from clio_sdk.models.matterbalancebase import MatterbalanceBaseIn, MatterbalancebaseOut, MatterbalancebaseUpdate, MatterbalancebaseDb
from clio_client.models.matter_balance_base import MatterBalanceBase

def convert_sdk_to_matterbalancebaseout(src: MatterBalanceBase) -> MatterbalancebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MatterbalancebaseOut(**src.model_dump())

def convert_matterbalancebasein_to_sdk(src: MatterbalanceBaseIn) -> MatterBalanceBase:
    """Converts a clio_sdk model to clio_client model."""
    return MatterBalanceBase(**src.model_dump())
