# Adapter for matterbudgetbase
from clio_sdk.models.matterbudgetbase import MatterbudgetbaseIn, MatterbudgetbaseOut, MatterbudgetbaseUpdate, MatterbudgetbaseDb
from clio_client.models import matter_budget_base

def convert_sdk_to_matterbudgetbaseout(src: matter_budget_base) -> MatterbudgetbaseOut:
    return MatterbudgetbaseOut(**src.dict())

def convert_matterbudgetbasein_to_sdk(src: MatterbudgetbaseIn) -> matter_budget_base:
    return matter_budget_base(**src.dict())
