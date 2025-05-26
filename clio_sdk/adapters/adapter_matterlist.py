# Adapter for matterlist
from clio_sdk.models.matterlist import MatterlistIn, MatterlistOut, MatterlistUpdate, MatterlistDb
from clio_client.models import matter_list

def convert_sdk_to_matterlistout(src: matter_list) -> MatterlistOut:
    return MatterlistOut(**src.dict())

def convert_matterlistin_to_sdk(src: MatterlistIn) -> matter_list:
    return matter_list(**src.dict())
