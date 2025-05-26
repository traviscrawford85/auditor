# Adapter for contingencyfeebase
from clio_sdk.models.contingencyfeebase import ContingencyfeeBaseIn, ContingencyfeebaseOut, ContingencyfeebaseUpdate, ContingencyfeebaseDb
from clio_client.models.contingency_fee_base import ContingencyFeeBase

def convert_sdk_to_contingencyfeebaseout(src: ContingencyFeeBase) -> ContingencyfeebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ContingencyfeebaseOut(**src.model_dump())

def convert_contingencyfeebasein_to_sdk(src: ContingencyfeeBaseIn) -> ContingencyFeeBase:
    """Converts a clio_sdk model to clio_client model."""
    return ContingencyFeeBase(**src.model_dump())
