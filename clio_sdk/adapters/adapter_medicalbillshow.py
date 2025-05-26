# Adapter for medicalbillshow
from clio_sdk.models.medicalbillshow import MedicalbillshowIn, MedicalbillshowOut, MedicalbillshowUpdate, MedicalbillshowDb
from clio_client.models import medical_bill_show

def convert_sdk_to_medicalbillshowout(src: medical_bill_show) -> MedicalbillshowOut:
    return MedicalbillshowOut(**src.dict())

def convert_medicalbillshowin_to_sdk(src: MedicalbillshowIn) -> medical_bill_show:
    return medical_bill_show(**src.dict())
