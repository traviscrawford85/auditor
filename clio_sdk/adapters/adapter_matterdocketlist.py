# Adapter for matterdocketlist
from clio_sdk.models.matterdocketlist import MatterdocketlistIn, MatterdocketlistOut, MatterdocketlistUpdate, MatterdocketlistDb
from clio_client.models import matter_docket_list

def convert_sdk_to_matterdocketlistout(src: matter_docket_list) -> MatterdocketlistOut:
    return MatterdocketlistOut(**src.dict())

def convert_matterdocketlistin_to_sdk(src: MatterdocketlistIn) -> matter_docket_list:
    return matter_docket_list(**src.dict())
