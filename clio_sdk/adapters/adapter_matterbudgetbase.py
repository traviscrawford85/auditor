# Adapter for matterbudgetbase
from clio_sdk.models.matterbudgetbase import MatterbudgetBaseIn, MatterbudgetbaseOut, MatterbudgetbaseUpdate, MatterbudgetbaseDb
from clio_client.models.matter_budget_base import MatterBudgetBase

def convert_sdk_to_matterbudgetbaseout(src: MatterBudgetBase) -> MatterbudgetbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MatterbudgetbaseOut(**src.model_dump())

def convert_matterbudgetbasein_to_sdk(src: MatterbudgetBaseIn) -> MatterBudgetBase:
    """Converts a clio_sdk model to clio_client model."""
    return MatterBudgetBase(**src.model_dump())
