# Adapter for mattercustomratebase
from clio_sdk.models.mattercustomratebase import MattercustomratebaseIn, MattercustomratebaseOut, MattercustomratebaseUpdate, MattercustomratebaseDb
from clio_client.models import matter_custom_rate

def convert_sdk_to_mattercustomratebaseout(src: matter_custom_rate) -> MattercustomratebaseOut:
    return MattercustomratebaseOut(**src.dict())

def convert_mattercustomratebasein_to_sdk(src: MattercustomratebaseIn) -> matter_custom_rate:
    return matter_custom_rate(**src.dict())
