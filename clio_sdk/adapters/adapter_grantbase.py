# Adapter for grantbase
from clio_sdk.models.grantbase import GrantBaseIn, GrantbaseOut, GrantbaseUpdate, GrantbaseDb
from clio_client.models.grant import Grant

def convert_sdk_to_grantbaseout(src: Grant) -> GrantbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return GrantbaseOut(**src.model_dump())

def convert_grantbasein_to_sdk(src: GrantBaseIn) -> Grant:
    """Converts a clio_sdk model to clio_client model."""
    return Grant(**src.model_dump())
