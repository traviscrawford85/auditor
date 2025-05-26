# Adapter for medicalbillbase
from clio_sdk.models.medicalbillbase import MedicalbillBaseIn, MedicalbillbaseOut, MedicalbillbaseUpdate, MedicalbillbaseDb
from clio_client.models.medical_bill import MedicalBill

def convert_sdk_to_medicalbillbaseout(src: MedicalBill) -> MedicalbillbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MedicalbillbaseOut(**src.model_dump())

def convert_medicalbillbasein_to_sdk(src: MedicalbillBaseIn) -> MedicalBill:
    """Converts a clio_sdk model to clio_client model."""
    return MedicalBill(**src.model_dump())
