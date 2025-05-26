# Adapter for matterdocketbase
from clio_sdk.models.matterdocketbase import MatterdocketbaseIn, MatterdocketbaseOut, MatterdocketbaseUpdate, MatterdocketbaseDb
from clio_client.models import matter_docket

def convert_sdk_to_matterdocketbaseout(src: matter_docket) -> MatterdocketbaseOut:
    return MatterdocketbaseOut(**src.dict())

def convert_matterdocketbasein_to_sdk(src: MatterdocketbaseIn) -> matter_docket:
    return matter_docket(**src.dict())
