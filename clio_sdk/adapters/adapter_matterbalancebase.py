# Adapter for matterbalancebase
from clio_sdk.models.matterbalancebase import MatterbalancebaseIn, MatterbalancebaseOut, MatterbalancebaseUpdate, MatterbalancebaseDb
from clio_client.models import matter_balance_base

def convert_sdk_to_matterbalancebaseout(src: matter_balance_base) -> MatterbalancebaseOut:
    return MatterbalancebaseOut(**src.dict())

def convert_matterbalancebasein_to_sdk(src: MatterbalancebaseIn) -> matter_balance_base:
    return matter_balance_base(**src.dict())
