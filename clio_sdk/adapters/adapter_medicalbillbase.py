# Adapter for medicalbillbase
from clio_sdk.models.medicalbillbase import MedicalbillbaseIn, MedicalbillbaseOut, MedicalbillbaseUpdate, MedicalbillbaseDb
from clio_client.models import medical_bill

def convert_sdk_to_medicalbillbaseout(src: medical_bill) -> MedicalbillbaseOut:
    return MedicalbillbaseOut(**src.dict())

def convert_medicalbillbasein_to_sdk(src: MedicalbillbaseIn) -> medical_bill:
    return medical_bill(**src.dict())
