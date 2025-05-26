# Adapter for grantbase
from clio_sdk.models.grantbase import GrantbaseIn, GrantbaseOut, GrantbaseUpdate, GrantbaseDb
from clio_client.models import grant

def convert_sdk_to_grantbaseout(src: grant) -> GrantbaseOut:
    return GrantbaseOut(**src.dict())

def convert_grantbasein_to_sdk(src: GrantbaseIn) -> grant:
    return grant(**src.dict())
