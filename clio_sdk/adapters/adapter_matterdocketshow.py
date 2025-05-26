# Adapter for matterdocketshow
from clio_sdk.models.matterdocketshow import MatterdocketshowIn, MatterdocketshowOut, MatterdocketshowUpdate, MatterdocketshowDb
from clio_client.models import matter_docket_show

def convert_sdk_to_matterdocketshowout(src: matter_docket_show) -> MatterdocketshowOut:
    return MatterdocketshowOut(**src.dict())

def convert_matterdocketshowin_to_sdk(src: MatterdocketshowIn) -> matter_docket_show:
    return matter_docket_show(**src.dict())
